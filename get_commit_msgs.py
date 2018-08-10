import os
import threading

import constants
import services
from repository import ReadRepositoryQueue
from request.request import ResponseStatusError
from utils import file_utils
from utils.log_utils import LOGGER
from utils.shell_args import SHELL_ARGS


class GetCommitError(Exception):
    pass


def _get_commits(repo_name):
    cur_page = 1

    try:
        first_page_commits, last_page = services.get_commits_by_repo_name(repo_name, cur_page, get_pages_total=True)
        if last_page > constants.COMMIT_PAGES_LIMIT:
            raise GetCommitError('commit_pages_total is greater than commit_pages_limit.')
    except ResponseStatusError:
            raise GetCommitError('This repo do not have master branch.')

    for commit in first_page_commits:
        yield {
            'sha': commit['sha'],
            'commit_msg': commit['commit']['message']
        }

    cur_page += 1
    while cur_page <= last_page:
        page_commits = services.get_commits_by_repo_name(repo_name, cur_page)
        for commit in page_commits:
            yield {
                'sha': commit['sha'],
                'commit_msg': commit['commit']['message']
            }
        cur_page += 1


def get_commit_msgs(repository_queue: ReadRepositoryQueue):
    repo = repository_queue.get()
    while repo:
        repo_name = repo['repo_name']
        try:
            commits = _get_commits(repo_name)
            last_commit_filenames = list()
            last_commit_path = ''

            repo_pos = repository_queue.pos()

            repo_path = os.path.join(constants.COMMIT_DATA_DIR, '%d.%s' % (repo_pos, repo_name.replace('/', '.')))
            # file_utils.safe_makedirs(repo_path)

            for commit_pos, commit in enumerate(commits):
                commit_sha = commit['sha']
                commit_msg = commit['commit_msg']

                commit_path = os.path.join(repo_path, '%d.%s' % (commit_pos, commit_sha))
                file_utils.safe_makedirs(commit_path)
                file_utils.write_string_to_file(os.path.join(commit_path, 'commit_msg'), commit_msg)

                try:
                    for last_commit_file_name in last_commit_filenames:
                        try:
                            last_commit_old_file_content = services.get_file_content(
                                repo_name, commit_sha, last_commit_file_name)
                        except ResponseStatusError:
                            last_commit_old_file_content = ''

                        file_utils.write_string_to_file(
                            os.path.join(last_commit_path, last_commit_file_name.replace('/', '.'), 'old_content'),
                            last_commit_old_file_content)

                    last_commit_filenames = list()
                    last_commit_path = commit_path

                    commit_detail = services.get_commit_detail(repo_name, commit_sha)
                    if commit_msg.startswith('Merge') or commit_msg.startswith('merge'):
                        file_utils.write_string_to_file(
                            os.path.join(commit_path, 'error'), 'This is a merge commmit')
                        continue

                    files = commit_detail['files']
                    if len(files) > constants.COMMIT_FILES_LIMIT:
                        file_utils.write_string_to_file(os.path.join(
                            commit_path, 'error'), 'files_len > COMMIT_FILES_LIMIT')
                        continue

                    for file in files:
                        filename = file['filename']
                        commit_file_path = os.path.join(commit_path, filename.replace('/', '.'))
                        file_utils.safe_makedirs(commit_file_path)

                        file_patch = file['patch'] if 'patch' in file else ''
                        file_utils.write_string_to_file(os.path.join(commit_file_path, 'patch'), file_patch)

                        new_file_content = services.get_file_content(repo_name, commit_sha, filename)
                        file_utils.write_string_to_file(os.path.join(commit_file_path, 'new_content'), new_file_content)

                        last_commit_filenames.append(filename)
                except Exception as error:
                    LOGGER.error('The unknown exception: %s' % str(error))
                    # shutil.rmtree(commit_path, ignore_errors=True)
            repository_queue.update_repo_status(repo['_id'], constants.REPO_STATUS['SUCCESS'])

            LOGGER.info('This repo has done, repo_pos: %d, repo_name: %s' % (repo_pos, repo_name))
        except GetCommitError as error:
            repository_queue.update_repo_status(repo['_id'], constants.REPO_STATUS['ERROR'], str(error))
            LOGGER.error(
                'This repo has error, repo_pos: %d, repo_name: %s, error: %s' % (repo_pos, repo_name, str(error)))
        except Exception as error:
            LOGGER.error('The unknown exception: %s' % str(error))

        repo = repository_queue.get()


def main():
    repository_queue = ReadRepositoryQueue(SHELL_ARGS.repos_skip)

    threads = []

    for _ in range(constants.THREAD_TOTAL):
        thread = threading.Thread(target=get_commit_msgs, args=(repository_queue,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
