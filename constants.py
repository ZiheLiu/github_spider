import os

from utils.shell_args import SHELL_ARGS

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

# for github
GITHUB_ACCOUNTS = [
    {
        'username': '272910663@qq.com',
        'password': 'ddyynls1015'
    },
    {
        'username': '1376260753@qq.com',
        'password': '_yamsm_28_'
    }
]

BUCKET_SIZE = 5
RATE = 4900 * len(GITHUB_ACCOUNTS) / 3600

USERNAME = 'xinleima'
PASSWORD = '_yamsm_28_'


GITHUB_DOMAIN = 'https://api.github.com'

# for project
LOGGING_FILENAME = os.path.join(STATIC_DIR, 'logs')
COMMIT_MSGS_FILENAME = os.path.join(STATIC_DIR, 'commitmsgs')

# for mongodb
DATABASE = {
    'HOST': 'localhost',
    'PORT': 27017,
    'DATABASE': 'github2'
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
COMMIT_PAGES_LIMIT = SHELL_ARGS.commits_limit
COMMIT_FILES_LIMIT = 10

COMMIT_DATA_DIR = os.path.join(STATIC_DIR, 'commits2')

THREAD_TOTAL = 5
