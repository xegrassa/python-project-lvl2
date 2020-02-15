from gendiff.factory import get_value
from gendiff.factory import get_status


ADD = 'add'
DEL = 'del'
NOT = 'not'
CHG = 'change'


def gen_string(indent, value, key, status):
    if status == ADD:
        prefix = '+'
    elif status == DEL:
        prefix = '-'
    elif status == CHG:
        return  gen_string(indent, value[1], key, ADD) + gen_string(indent, value[0], key, DEL)
    else:
        prefix = ' '
    if value == None:
        return "{}{} {}: ".format(indent[:-2], prefix, key)
    return "{}{} {}: {}\n".format(indent[:-2], prefix, key, value)


def render_text(diff, deep=1):
    indent = '    ' * deep
    render = '{\n'
    for key in sorted(diff):
        if isinstance(get_value(diff, key), dict):
            render += gen_string(indent, None, key, get_status(diff, key))
            render += render_text(get_value(diff, key), deep + 1)
        else:
            render += gen_string(indent, get_value(diff, key), key, get_status(diff, key))
    render += indent[:-4] + '}\n'
    return render
