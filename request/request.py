import random
import threading

import requests
from simplejson import JSONDecodeError

import constants
from utils.log_utils import LOGGER
from .bucket import Bucket


# _bucket = Bucket()


class ResponseStatusError(Exception):
    pass


def _get_err_msg(res):
    try:
        return res.json()
    except JSONDecodeError:
        return res.text


class Request(object):
    def __init__(self):
        self._bucket = Bucket()
        self._accounts_index = 0
        self._lock = threading.RLock()

    def _get_account(self):
        self._lock.acquire()
        github_account = constants.GITHUB_ACCOUNTS[self._accounts_index]
        LOGGER.info('username: %s' % github_account['username'])
        self._accounts_index = (self._accounts_index + 1) % len(constants.GITHUB_ACCOUNTS)
        self._lock.release()
        return github_account

    def get(self, url: str, headers=None):
        self._bucket.get()

        if not url.startswith('http'):
            url = constants.GITHUB_DOMAIN + url

        LOGGER.info('get [%s]' % url)

        must_headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
        if headers:
            headers.update(must_headers)

        github_account = self._get_account()

        res = requests.get(url,
                           headers=headers,
                           auth=(github_account['username'], github_account['password']),
                           stream=True)

        if res.status_code != 200:
            raise ResponseStatusError(_get_err_msg(res))

        return res


REQUEST = Request()
