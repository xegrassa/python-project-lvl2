from gendiff.factory import get_value
from gendiff.factory import get_status


ADD = 'add'
DEL = 'del'
NOT = 'not'
CHG = 'change'


def gen_string(value, key, status, path_keys=None):
    path = '.'.join(path_keys + [key])
    if isinstance(value, dict):
        value = 'complex value'
    if status == ADD:
        return "Property '{}' was added with value: '{}'\n".format(path, value)
    elif status == DEL:
        return "Property '{}' was removed\n".format(path)
    elif status == CHG:
        return ("Property '{}' was changed. From '{}' to '{}'\n"
                .format(path, value[0], value[1]))
    return ''


def render_plain(diff, path_keys=[]):
    render = ''
    for key in sorted(diff):
        if get_status(diff, key) == NOT and isinstance(get_value(diff, key),
                                                       dict):
            path_keys.append(key)
            render += render_plain(get_value(diff, key), path_keys)
            path_keys.pop()
            continue
        render += gen_string(get_value(diff, key), key,
                             get_status(diff, key), path_keys)
    return render
