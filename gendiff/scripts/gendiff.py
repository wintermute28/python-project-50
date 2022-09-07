#!/usr/bin/env python3
import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

def generate_diff(file1, file2):
    result = "{\n"
    first_file = json.load(open(file1))
    second_file = json.load(open(file2))
    keys = sorted(list({x for x in {**first_file, **second_file}}))
    for key in keys:
        if first_file.get(key) == second_file.get(key):
            result += f"    {key}: {bool_convert(second_file[key])}\n"
            continue
        if first_file.get(key) is None:
            result += f"  + {key}: {bool_convert(second_file[key])}\n"
            continue
        if second_file.get(key) is None:
            result += f"  - {key}: {bool_convert(first_file[key])}\n"
            continue
        if first_file.get(key) != second_file.get(key):
            result += f"  - {key}: {bool_convert(first_file[key])}\n"
            result += f"  + {key}: {bool_convert(second_file[key])}\n"
    result += "}"
    return result

def bool_convert(input):
    if input is True:
        input = 'true'
    if input is False:
        input = 'false'
    return str(input)


if __name__ == "__main__":
    main()
