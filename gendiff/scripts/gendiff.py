import argparse
from gendiff import parsers
from gendiff import format


ADD = 'add'
DEL = 'del'
NOT = 'not'
CHG = 'change'


def gen_key_process(file, keys, change):
    record_to_diff = dict(map(lambda key: (key, (file[key], change)), keys))
    return record_to_diff


def generate_diff(prs_file1, prs_file2):
    diff = {}
    keys_first_pars_obj = set(prs_file1.keys())
    keys_second_pars_obj = set(prs_file2.keys())
    del_keys = keys_first_pars_obj.difference(keys_second_pars_obj)
    add_keys = keys_second_pars_obj.difference(keys_first_pars_obj)
    equal_keys = set(prs_file1.keys()).intersection(set(prs_file2.keys()))

    for key in equal_keys:
        if isinstance(prs_file1[key], dict) and isinstance(prs_file2[key], dict):
            diff.update({key: (generate_diff(prs_file1[key], prs_file2[key]), NOT)})
        elif prs_file1[key] == prs_file2[key]:
            diff.update(gen_key_process(prs_file1, (key,), NOT))
        else:
            diff.update({key: ((prs_file1[key], prs_file2[key]), CHG)})

    diff.update(gen_key_process(prs_file1, del_keys, DEL))
    diff.update(gen_key_process(prs_file2, add_keys, ADD))
    return diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='text', help="set format of output",
                        type=format.get_render)
    args = parser.parse_args()
    prs_file1 = parsers.parse_file(args.first_file)
    prs_file2 = parsers.parse_file(args.second_file)
    diff = generate_diff(prs_file1, prs_file2)
    print(args.format(diff))


if __name__ == '__main__':
    main()
