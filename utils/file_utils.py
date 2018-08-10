import codecs
import os


def write_string_to_file(filename, content):
    with codecs.open(filename, 'w', encoding='utf-8') as fout:
        fout.write(content)


def safe_makedirs(dir_name):
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)


def dirs_count(root_dir, depth):
    if not os.path.isdir(root_dir):
        return 0
    if depth == 0:
        return 1

    items_count = 0
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        items_count += dirs_count(item_path, depth - 1)
    return items_count
