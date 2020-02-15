from gendiff.factory import get_value
from gendiff.factory import get_status


ADD = 'add'
DEL = 'del'
NOT = 'not'
CHG = 'change'


def gen_string(indent, diff, key, status):
    if status == ADD:
        prefix = '+'
    elif status == DEL:
        prefix = '-'
    elif status == CHG:
        return gen_string(indent, diff, key, DEL) + gen_string(indent, diff, key, ADD)
    else:
        prefix = ' '
    if diff == None:
        return "{}{} {}: ".format(indent[:-2], prefix, key)
    return "{}{} {}: {}\n".format(indent[:-2], prefix, key, get_value(diff, key))


def render_text(diff, deep=1):
    indent = '    ' * deep
    render = '{\n'
    for key in diff:
        if isinstance(get_value(diff, key), dict):
            render += gen_string(indent, None, key, get_status(diff, key))
            render += render_text(get_value(diff, key), deep + 1)
        else:
            render += gen_string(indent, diff, key, get_status(diff, key))
    render += indent[:-4] + '}\n'
    return render
