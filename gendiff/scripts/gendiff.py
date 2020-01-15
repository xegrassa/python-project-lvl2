import argparse
from gendiff import parsers


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args()
    file1 = parsers.parse_file(args.first_file)
    file2 = parsers.parse_file(args.second_file)
    z = parsers.generate_diff(file1, file2)
    print(z)
    print(parsers.render_classic(z))


if __name__ == '__main__':
    main()
