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
    res = requests.get(url,
                       headers=headers,
                       auth=(constants.USERNAME, constants.PASSWORD))

    if res.status_code != 200:
        raise ResponseStatusError(_get_err_msg(res))

    return res
