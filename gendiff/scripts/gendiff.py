import argparse
import os.path
from gendiff import parsers
from gendiff import format


# def generate_diff(file1, file2):
#     diff = {}
#     for key in file1:
#         if key in file2:
#             if isinstance(file1[key], dict) and isinstance(file2[key], dict):
#                 diff[key] = {'value': generate_diff(file1[key], file2[key]),
#                              'change': 'not'}
#             elif file1[key] != file2[key]:
#                 diff[key] = [{'value': file2[key], 'change': 'add'},
#                              {'value': file1[key], 'change': 'del'}]
#             elif file1[key] == file2[key]:
#                 diff[key] = {'value': file1[key], 'change': 'not'}
#         else:
#             diff[key] = {'value': file1[key], 'change': 'del'}
#     for key in file2:
#         if key not in file1:
#             diff[key] = {'value': file2[key], 'change': 'add'}
#     return diff
ADD = 'add'
DEL = 'del'
NOT = 'not'
CHG = 'change'


def gen_key_process(file, keys, change):
    record_to_diff = dict(map(lambda key: (key, (file[key], change)), keys))
    return record_to_diff


def generate_diff(file1, file2):
    diff = {}
    keys_first_pars_obj = set(file1.keys())
    keys_second_pars_obj = set(file2.keys())
    del_keys = keys_first_pars_obj.difference(keys_second_pars_obj)
    add_keys = keys_second_pars_obj.difference(keys_first_pars_obj)
    equal_keys = set(file1.keys()).intersection(set(file2.keys()))

    for key in equal_keys:
        if isinstance(file1[key],dict) and isinstance(file2[key], dict):
            diff.update({key: (generate_diff(file1[key], file2[key]), NOT)})
        elif file1[key] == file2[key]:
            diff.update(gen_key_process(file1, (key,), NOT))
        else:
            diff.update({key: ((file1[key], file2[key]), CHG)})

    diff.update(gen_key_process(file1, del_keys, DEL))
    diff.update(gen_key_process(file2, add_keys, ADD))
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
    # diff = generate_diff(file1, file2)
    # print(args.format(diff))
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
