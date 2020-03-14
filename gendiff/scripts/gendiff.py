import argparse
from gendiff import parsers
from gendiff import format
from gendiff import build_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='text', help="set format of output",
                        type=format.get_render)
    args = parser.parse_args()
    try:
        prs_file1 = parsers.parse_file(args.first_file)
        prs_file2 = parsers.parse_file(args.second_file)
    except Warning:
        print('Неправильное расширение файла')
    else:
        diff = build_diff.generate_diff(prs_file1, prs_file2)
        print(args.format(diff))


if __name__ == '__main__':
    main()
