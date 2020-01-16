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

