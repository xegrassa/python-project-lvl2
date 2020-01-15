import json
import yaml


def is_json(path_file):
    if path_file[path_file.rfind('.'):] == '.json':
        return True
    return False


def parse_file(path_file):
    if is_json(path_file):
        return json.load(open(path_file))
    return yaml.safe_load(open(path_file))


def gen_single_string(key, value, indent):
    return "{}{}{}: {}\n".format(indent[:-2], value['change_prefix'],
                                 key, value['value'])


def generate_diff(file1, file2):
    diff = {}
    for key in file1:
        if key in file2:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                diff[key] = {'value': generate_diff(file1[key], file2[key]),
                             'change_prefix': '  '}
            elif file1[key] != file2[key]:
                diff[key] = [{'value': file2[key], 'change_prefix': '+ '},
                             {'value': file1[key], 'change_prefix': '- '}]
            elif file1[key] == file2[key]:
                diff[key] = {'value': file1[key], 'change_prefix': '  '}
        else:
            diff[key] = {'value': file1[key], 'change_prefix': '- '}
    for key in file2:
        if key not in file1:
            diff[key] = {'value': file2[key], 'change_prefix': '+ '}
    return diff


def render_classic(diff, deep=1):
    indent = '    ' * deep
    render = '{\n'
    try:
        for key in diff:

            if isinstance(diff[key], list):
                render += gen_single_string(key, diff[key][0], indent)
                render += gen_single_string(key, diff[key][1], indent)
            elif isinstance(diff[key].get('value', False), dict):
                render += "{}{}{}: ".format(indent[:-2],
                                            diff[key]['change_prefix'], key)
                render += render_classic(diff[key]['value'], deep + 1)
            else:
                render += gen_single_string(key, diff[key], indent)
    except:
        render += "{}{}: {}\n".format(indent, key, diff[key])
    render += indent[:-4] + '}\n'
    return render
