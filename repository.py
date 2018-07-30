import services


class Repository(object):
    def __init__(self, repos_sum, max_starts_count=None):
        self.repos_sum = repos_sum
        self.max_starts_count = max_starts_count

    def repositories(self):
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


if __name__ == '__main__':
    repos = Repository(1001)
    for repo in repos.repositories():
        print(repo)
