import requests

from .bucket import Bucket

_bucket = Bucket()


def get(url: str, headers=None):
    _bucket.get()

    res = requests.get(url, headers=headers)

    return res
