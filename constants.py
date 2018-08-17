import os

from utils.shell_args import SHELL_ARGS

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

# for github
GITHUB_ACCOUNTS = [
    {
        'username': 'nvk076@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'nwx261@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'kha165@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'pzi957@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'llk874@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'yfx936@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'mbw416@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'zop489@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'hla851@163.com',
        'password': 'ddyynls1015'
    },
    {
        'username': 'vbc647@163.com',
        'password': 'ddyynls1015'
    }
]

BUCKET_SIZE = 5
RATE = 4000 * len(GITHUB_ACCOUNTS) / 3600

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
COMMIT_PAGES_LIMIT = SHELL_ARGS.commits_limit
COMMIT_FILES_LIMIT = 10

COMMIT_DATA_DIR = os.path.join(STATIC_DIR, 'commits')

THREAD_TOTAL = 5
