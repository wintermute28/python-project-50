#!/usr/bin/env python3
from gendiff.parsing import parcing_arguments
from gendiff.diff import generate_diff


def main():
    args = parcing_arguments()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
