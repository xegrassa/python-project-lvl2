import argparse
from gendiff import parsers
from gendiff import format
import os.path


def generate_diff(file1, file2):
    diff = {}
    for key in file1:
        if key in file2:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                diff[key] = {'value': generate_diff(file1[key], file2[key]),
                             'change': 'not'}
            elif file1[key] != file2[key]:
                diff[key] = [{'value': file2[key], 'change': 'add'},
                             {'value': file1[key], 'change': 'del'}]
            elif file1[key] == file2[key]:
                diff[key] = {'value': file1[key], 'change': 'not'}
        else:
            diff[key] = {'value': file1[key], 'change': 'del'}
    for key in file2:
        if key not in file1:
            diff[key] = {'value': file2[key], 'change': 'add'}
    return diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='text', help="set format of output",
                        type=format.get_render)
    args = parser.parse_args()
    file1 = parsers.parse_file(args.first_file)
    file2 = parsers.parse_file(args.second_file)
    diff = generate_diff(file1, file2)
    print(args.format(diff))
    print(os.path.splitext(args.first_file)[1])


if __name__ == '__main__':
    main()
