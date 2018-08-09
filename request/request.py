import requests

import constants
from utils.log_utils import LOGGER
from .bucket import Bucket

_bucket = Bucket()


class ResponseStatusError(Exception):
    pass


def _get_err_msg(res):
    try:
        return res.text()
    except TypeError:
        return res.json()


def get(url: str, headers=None):
    _bucket.get()

    LOGGER.info('get [%s]' % url)
    res = requests.get(constants.GITHUB_DOMAIN + url,
                       headers=headers,
                       auth=(constants.USERNAME, constants.PASSWORD))

    if res.status_code != 200:
        raise ResponseStatusError(_get_err_msg(res))

    return res
