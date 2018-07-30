import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

# for github
BUCKET_SIZE = 5
RATE = 5000 / 3600

USERNAME = 'xinleima'
PASSWORD = '_yamsm_28_'

GITHUB_DOMAIN = 'https://api.github.com'

# for project
LOGGING_FILENAME = os.path.join(STATIC_DIR, 'logs')

# for mongodb
DATABASE = {
    'HOST': 'localhost',
    'PORT': 27017,
    'DATABASE': 'github'
}

DB_COLLECTIONS = {
    'BRIEF_REPOS': 'brief_repos'
}
