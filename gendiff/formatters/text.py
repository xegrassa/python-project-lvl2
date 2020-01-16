def gen_single_string(key, value, indent):
    return "{}{}{}: {}\n".format(indent[:-2], value['change_prefix'],
                                 key, value['value'])


def render_text(diff, deep=1):
    indent = '    ' * deep
    render = '{\n'
    for key in diff:
        if isinstance(diff[key], (dict, list)):
            if isinstance(diff[key], list):
                render += gen_single_string(key, diff[key][0], indent)
                render += gen_single_string(key, diff[key][1], indent)
            elif isinstance(diff[key].get('value', False), dict):
                render += "{}{}{}: ".format(indent[:-2],
                                            diff[key]['change_prefix'], key)
                render += render_text(diff[key]['value'], deep + 1)
            else:
                render += gen_single_string(key, diff[key], indent)
        else:
            render += "{}{}: {}\n".format(indent, key, diff[key])
    render += indent[:-4] + '}\n'
    return render