import requests

import constants
from utils.log_utils import LOGGER
from .bucket import Bucket

_bucket = Bucket()


def get(url: str, headers=None):
    _bucket.get()

    LOGGER.info('get [%s]' % url)
    res = requests.get(constants.GITHUB_DOMAIN + url,
                       headers=headers,
                       auth=(constants.USERNAME, constants.PASSWORD))

    return res
