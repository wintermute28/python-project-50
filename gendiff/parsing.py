#!/usr/bin/env python
import json
import yaml
import argparse
from gendiff.stylish import stylish


def files_parser(file1, file2):
    files_in = (file1, file2)
    files_out = []
    for file_in in files_in:
        if '.json' in file_in:
            file = json.load(open(file_in))
        elif '.yml' or '.yaml' in file_in:
            file = yaml.load(open(file_in), Loader=yaml.SafeLoader)
        files_out.append(file)
    return files_out


def parcing_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default=stylish,
                        help='set format of output'
                        )
    args = parser.parse_args()
    return args
