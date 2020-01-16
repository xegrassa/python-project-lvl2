import argparse
from gendiff import parsers
from gendiff import gendiff
from gendiff.formatters.text import render_text
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args()
    file1 = parsers.parse_file(args.first_file)
    file2 = parsers.parse_file(args.second_file)
    diff_beetwen_files = gendiff.generate_diff(file1, file2)
    if args.format == 'plain':
        print(render_plain(diff_beetwen_files))
    elif args.format == 'json':
        print(render_json(diff_beetwen_files))
    else:
        print(render_text(diff_beetwen_files))


if __name__ == '__main__':
    main()
