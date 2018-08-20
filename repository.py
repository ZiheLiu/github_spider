from queue import Queue, Empty

from pymongo import MongoClient

import constants
import services


class WriteRepository(object):
    def __init__(self, repos_sum, max_starts_count=None):
        self.repos_sum = repos_sum
        self.max_starts_count = max_starts_count

    def repositories(self):
        """Get brief repository lazy list.

        Return:
            Iterable list of object. The object's keys include 'url' and 'repo_name'.
        """
        max_starts_count = self.max_starts_count
        last_repo_name = None

        repos_count = 0
        while True:
            for page in range(1, 11):
                brief_repos = services.get_repositories(page, max_starts_count)
                for brief_repo in brief_repos:
                    url = brief_repo['url']
                    repo_name = url.replace('https://api.github.com/repos/', '')
                    last_repo_name = repo_name
                    yield {
                        'url': url,
                        'repo_name': repo_name
                    }

                    repos_count += 1
                    if repos_count >= self.repos_sum:
                        return
            last_repo_info = services.get_repository(last_repo_name)
            max_starts_count = last_repo_info['stargazers_count']


class ReadRepositoryQueue(object):
    def __init__(self, skip=0):
        conn = MongoClient(constants.DATABASE['HOST'], constants.DATABASE['PORT'])[constants.DATABASE['DATABASE']]
        self._db_col = conn[constants.DB_COLLECTIONS['BRIEF_REPOS']]
        self._total = self._db_col.count()
        self._repos_queue = self._get_repos_queue(skip)

    def _get_repos_queue(self, skip):
        queue = Queue()
        with self._db_col.find() as repos:
            for idx, repo in enumerate(repos):
                if idx < skip:
                    continue
                # if 'status' not in repo or repo['status'] == constants.REPO_STATUS['NO_DEAL']:
                queue.put(repo)
        return queue

    def get(self):
        try:
            return self._repos_queue.get(block=False)
        except Empty:
            return None

    def size(self):
        return self._repos_queue.qsize()

    def pos(self):
        return self._total - self.size()

    def update_repo_status(self, repo_id, repo_status, repo_error_msg=None):
        update_data = {'status': repo_status}
        if repo_error_msg:
            update_data['error_msg'] = repo_error_msg
        self._db_col.update({'_id': repo_id}, {'$set': update_data})


def write_repos2db():
    brief_repos = list(WriteRepository(4000).repositories())
    conn = MongoClient(constants.DATABASE['HOST'], constants.DATABASE['PORT'])[constants.DATABASE['DATABASE']]
    brief_repos_col = conn[constants.DB_COLLECTIONS['BRIEF_REPOS']]
    brief_repos_col.insert(brief_repos)


def get_brief_repos():
    """Get brief information of repositories.

    Return:
        list of object. The object's keys include '_id', 'url' and 'repo_name'.
    """
    conn = MongoClient(constants.DATABASE['HOST'], constants.DATABASE['PORT'])[constants.DATABASE['DATABASE']]
    brief_repos_col = conn[constants.DB_COLLECTIONS['BRIEF_REPOS']]
    with brief_repos_col.find() as items:
        brief_repos = list(items)
    return brief_repos


if __name__ == '__main__':
    write_repos2db()
