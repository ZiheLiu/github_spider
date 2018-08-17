import argparse

import constants


def add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument('--username', type=str, default=constants.USERNAME)
    parser.add_argument('--password', type=str, default=constants.PASSWORD)
    parser.add_argument('--repos_skip', type=int, default=0)
    parser.add_argument('--commits_limit', type=int, default=10)


parser = argparse.ArgumentParser()
add_arguments(parser)
SHELL_ARGS = parser.parse_args()
