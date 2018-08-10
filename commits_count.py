import constants
from utils import file_utils


def commits_count():
    root_dir = constants.COMMIT_DATA_DIR
    depth = 2
    print('The commits dir: %s, depth: %d' % (root_dir, depth))
    print(file_utils.dirs_count(root_dir, depth))


if __name__ == '__main__':
    commits_count()
