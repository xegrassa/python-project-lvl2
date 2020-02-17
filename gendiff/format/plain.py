from gendiff.factory import get_value
from gendiff.factory import get_status


ADD = 'add'
DEL = 'del'
NOT = 'not'
CHG = 'change'


def gen_string(value, key, status):
    if isinstance(value, dict):
        value = 'complex value'
    if status == ADD:
        return "Property '{}' was added with value: '{}'\n".format(key, value)
    elif status == DEL:
        return "Property '{}' was removed\n".format(key)
    elif status == CHG:
        return "Property '{}' was changed. From '{}' to '{}'\n".format(key, value[0], value[1])
    return ''


def render_plain(diff):
    print(diff)
    render = ''
    for key in diff:
        if get_status(diff, key) == NOT and isinstance(get_value(diff, key), dict):
            render +='{}.{}'.format(key, render_plain(get_value(diff, key)))
            continue
        # print(key)
        render += gen_string(get_value(diff,key), key, get_status(diff, key))
    return render



# def gen_string_del(key):
#     return "Property '{}' was removed\n".format(key)


# def gen_string_add(key, value):
#     if isinstance(value, dict):
#         value = 'complex value'
#     return "Property '{}' was added with value: '{}'\n".format(key, value)


# def gen_string_change(key, value):
#     return "Property '{}' was changed. From '{}' to '{}'\n"\
#             .format(key, value[1]['value'], value[0]['value'])


# def render_plain(diff, path_key=''):
#     render = '1'
#     if path_key:
#         path_key = path_key + '.'
#     for key in diff:
#         if isinstance(diff[key], dict):
#             if diff[key]['change'] == 'del':
#                 render += gen_string_del(path_key+key)
#             if diff[key]['change'] == 'add':
#                 render += gen_string_add(path_key+key, diff[key]['value'])
#             if (diff[key]['change'] == 'not' and
#                     isinstance(diff[key]['value'], dict)):
#                 render += render_plain(diff[key]['value'], path_key+key)
#         elif isinstance(diff[key], list):
#             render += gen_string_change(path_key+key, diff[key])
#     return render
