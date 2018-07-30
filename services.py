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
    url = '/repos/' + repo_name
    res = request.get(url)
    return res.json()
