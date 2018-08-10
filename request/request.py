import random

import requests
from simplejson import JSONDecodeError

import constants
from utils.log_utils import LOGGER
from .bucket import Bucket

_bucket = Bucket()


class ResponseStatusError(Exception):
    pass


def _get_err_msg(res):
    try:
        return res.json()
    except JSONDecodeError:
        return res.text


def get(url: str, headers=None):
    _bucket.get()

    if not url.startswith('http'):
        url = constants.GITHUB_DOMAIN + url

    LOGGER.info('get [%s]' % url)

    must_headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    if headers:
        headers.update(must_headers)

    github_account_index = random.randint(0, 4)
    github_account = constants.GITHUB_ACCOUNTS[github_account_index]

    res = requests.get(url,
                       headers=headers,
                       auth=(github_account['username'], github_account['password']),
                       stream=True)

    if res.status_code != 200:
        raise ResponseStatusError(_get_err_msg(res))

    return res
