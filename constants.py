import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

# for github
BUCKET_SIZE = 5
RATE = 4500 * 5 / 3600

USERNAME = 'xinleima'
PASSWORD = '_yamsm_28_'

GITHUB_ACCOUNTS = [
    {
        'username': 'xinleima',
        'password': '_yamsm_28_'
    },
    {
        'username': 'sxw196@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'mgs588@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'wom684@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'rwj918@163.com',
        'password': 'ddyynls1015'
    }
]

GITHUB_DOMAIN = 'https://api.github.com'

# for project
LOGGING_FILENAME = os.path.join(STATIC_DIR, 'logs')
COMMIT_MSGS_FILENAME = os.path.join(STATIC_DIR, 'commitmsgs')

# for mongodb
DATABASE = {
    'HOST': 'localhost',
    'PORT': 27017,
    'DATABASE': 'github'
}

DB_COLLECTIONS = {
    'BRIEF_REPOS': 'brief_repos'
}

REPO_STATUS = {
    'NO_DEAL': 0,
    'SUCCESS': 1,
    'ERROR': 2
}

# for data
COMMIT_PAGES_LIMIT = 10
COMMIT_FILES_LIMIT = 10

COMMIT_DATA_DIR = os.path.join(STATIC_DIR, 'commits')

THREAD_TOTAL = 5
