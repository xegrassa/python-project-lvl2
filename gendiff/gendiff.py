def generate_diff(file1, file2):
    diff = {}
    for key in file1:
        if key in file2:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                diff[key] = {'value': generate_diff(file1[key], file2[key]),
                             'change': 'not'}
            elif file1[key] != file2[key]:
                diff[key] = [{'value': file2[key], 'change': 'add'},
                             {'value': file1[key], 'change': 'del'}]
            elif file1[key] == file2[key]:
                diff[key] = {'value': file1[key], 'change': 'not'}
        else:
            diff[key] = {'value': file1[key], 'change': 'del'}
    for key in file2:
        if key not in file1:
            diff[key] = {'value': file2[key], 'change': 'add'}
    return diff
