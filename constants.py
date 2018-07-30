import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

BUCKET_SIZE = 5
RATE = 5000 / 3600

USERNAME = 'xinleima'
PASSWORD = '_yamsm_28_'

GITHUB_DOMAIN = 'https://api.github.com'

LOGGING_FILENAME = os.path.join(STATIC_DIR, 'logs')
