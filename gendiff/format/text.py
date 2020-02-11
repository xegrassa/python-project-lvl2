from gendiff.factory import get_value
from gendiff.factory import get_status


ADD = 'add'
DEL = 'del'
NOT = 'not'
CHG = 'change'


# def gen_single_string(key, value, indent):
#     if value['change'] == 'add':
#         prefix = '+ '
#     elif value['change'] == 'del':
#         prefix = '- '
#     elif value['change'] == 'not':
#         prefix = '  '
#     return "{}{}{}: {}\n".format(indent[:-2], prefix, key, value['value'])


# def gen_begin_complex_string(indent, value, key):
#     if value['change'] == 'add':
#         prefix = '+ '
#     elif value['change'] == 'del':
#         prefix = '- '
#     elif value['change'] == 'not':
#         prefix = '  '
#     return "{}{}{}: ".format(indent[:-2], prefix, key)


# def render_text(diff, deep=1):
#     indent = '    ' * deep
#     render = '{\n'
#     for key in diff:
#         if isinstance(diff[key], (dict, list)):
#             if isinstance(diff[key], list):
#                 render += gen_single_string(key, diff[key][0], indent)
#                 render += gen_single_string(key, diff[key][1], indent)
#             elif isinstance(diff[key].get('value', False), dict):
#                 render += gen_begin_complex_string(indent, diff[key], key)
#                 render += render_text(diff[key]['value'], deep + 1)
#             else:
#                 render += gen_single_string(key, diff[key], indent)
#         else:
#             render += "{}{}: {}\n".format(indent, key, diff[key])
#     render += indent[:-4] + '}\n'
    # return render


def gen_string(diff, key, status):
    if status == ADD:
        prefix = '+'
    elif status == DEL:
        prefix = '-'
    elif status == NOT:
        prefix = ' '
    else:
        prefix = 'xz'
    return "{} {}: {}\n".format(prefix, key, get_value(diff, key))


def render_text(diff, deep=1):
    indent = '    ' * deep
    render = '{\n'
    for key in diff:
        # if get_status(diff, key) != ADD:
        render+= gen_string(diff, key, get_status(diff,key) )
    return render



