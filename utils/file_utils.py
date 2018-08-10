import codecs
import os


def write_string_to_file(filename, content):
    with codecs.open(filename, 'w', encoding='utf-8') as fout:
        fout.write(content)


def safe_makedirs(dir_name):
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
