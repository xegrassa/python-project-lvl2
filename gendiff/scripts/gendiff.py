import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


def generate_diff(path_to_file1, path_to_file2):
    file1 = json.load(open(path_to_file1))
    file2 = json.load(open(path_to_file2))
    set_no_change = (set(file1.items()) &
                     set(file2.items()))
    set_adding = {(i, file2[i]) for i in (set(file2.keys()) -
                                          set(file1.keys()))}
    set_deleting = {(i, file1[i]) for i in (set(file1.keys()) -
                                            set(file2.keys()))}
    set_changing = (set(file1) & set(file2)) - set(dict(set_no_change).keys())
    diff = "{\n"
    for i in set_no_change:
        diff += "      {}: {}\n".format(i[0], i[1])
    for i in set_adding:
        diff += "    + {}: {}\n".format(i[0], i[1])
    for i in set_changing:
        diff += "    - {}: {}\n".format(i, file1[i])
        diff += "    + {}: {}\n".format(i, file2[i])
    for i in set_deleting:
        diff += "    - {}: {}\n".format(i[0], i[1])
    diff += "}"
    return diff


if __name__ == '__main__':
    main()
