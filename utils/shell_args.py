import argparse


def add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument('--repos_skip', type=int, default=0)
    parser.add_argument('--commits_limit', type=int, default=10)
    parser.add_argument('--output_dir', type=str, default='commits')


parser = argparse.ArgumentParser()
add_arguments(parser)
SHELL_ARGS = parser.parse_args()
