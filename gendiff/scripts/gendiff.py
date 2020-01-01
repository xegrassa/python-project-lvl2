import argparse


def main():
    USAGE = 'usage: gendiff [-h] [-f FORMAT] first_file second_file'
    parser = argparse.ArgumentParser(usage=USAGE, description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help=argparse.SUPPRESS)
    parser.parse_args()


if __name__ == '__main__':
    main()
