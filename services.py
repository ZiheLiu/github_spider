import re
from urllib import parse

from request import request


def get_repositories(cur_page, max_starts_count=None):
    """按照star数目递减的顺序，获得star数目上限为max_starts_count的Java仓库概述信息."""
    if max_starts_count:
        url_starts_part = '+stars:<%d' % max_starts_count
    else:
        url_starts_part = ''

    url = '/search/repositories?q=language:java%s&page=%d&per_page=100' % (url_starts_part, cur_page)
    res = request.get(url)
    return res.json()['items']


def get_repository(repo_name):
    """根据仓库名称，获取仓库详情."""
    url = '/repos/' + repo_name
    res = request.get(url)
    return res.json()


def get_commits_by_desc(desc):
    url = '/search/commits?q=' + desc
    res = request.get(url, {
        'Accept': 'application/vnd.github.cloak-preview+json'
    })
    return res.json()


def get_commits_by_repo_name(repo_name, cur_page, get_pages_total=False):
    """根据仓库名称，获取仓库的commit的列表（按照时间递减顺序）.

    Return:
        list of object.
    Example:
        [
            {
                'sha': 'the sha ID',
                'commit': {
                    'message': 'the commit message'
                }
            }
        ]
    """
    url = '/repos/%s/commits?per_page=100&page=%d&sha=master' % (repo_name, cur_page)
    res = request.get(url)

    if not get_pages_total:
        return res.json()

    link_str = res.headers['Link']
    last_page_link_search = re.search(', <(.*)>; rel="last"', link_str)
    last_page_link = last_page_link_search.group(1)
    pages_total = parse.parse_qs(parse.urlparse(last_page_link).query)['page'][0]

    return res.json(), pages_total


def get_commit_detail(repo_name, commit_sha):
    """根据仓库名称、commit的ID，获得commit的详细信息.

    Return:
        object.
    Example:
        {
            'files': [
                'filename': 'the file name',
                'patch': 'the file patch'
            ]
        }
    """
    url = '/repos/%s/commits/%s' % (repo_name, commit_sha)
    res = request.get(url, {
        'Accept': 'application/vnd.github.cloak-preview+json'
    })
    return res.json()


def get_file_content(repo_name, commit_sha, filename):
    """根据仓库名称、commit的ID、文件名称，获取文件的具体内容.

    Return:
        str. The file content string.
    """
    url = 'https://github.com/%s/raw/%s/%s' % (repo_name, commit_sha, filename)
    res = request.get(url)
    return res.text


if __name__ == '__main__':
    def main():
        commits = get_file_content('iluwatar/java-design-patterns',
                                   'facb9e51a6f88765682d1723a2e3601825e275f6',
                                   'reactor/src/main/java/com/iluwatar/reactor/app/AppClient.javas')
        print(commits)


    main()
