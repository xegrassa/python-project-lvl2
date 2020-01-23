def gen_string_del(key):
    return "Property '{}' was removed\n".format(key)


def gen_string_add(key, value):
    if isinstance(value, dict):
        value = 'complex value'
    return "Property '{}' was added with value: '{}'\n".format(key, value)


def gen_string_change(key, value):
    return "Property '{}' was changed. From '{}' to '{}'\n"\
            .format(key, value[1]['value'], value[0]['value'])


def render_plain(diff, path_key=''):
    render = ''
    if path_key:
        path_key = path_key + '.'
    for key in diff:
        if isinstance(diff[key], dict):
            if diff[key]['change'] == 'del':
                render += gen_string_del(path_key+key)
            if diff[key]['change'] == 'add':
                render += gen_string_add(path_key+key, diff[key]['value'])
            if (diff[key]['change'] == 'not' and
                    isinstance(diff[key]['value'], dict)):
                render += render_plain(diff[key]['value'], path_key+key)
        elif isinstance(diff[key], list):
            render += gen_string_change(path_key+key, diff[key])
    return render
