ADD = 'add'
DEL = 'del'
NOT = 'not'
CHG = 'change'


def get_value(diff, key):
    if isinstance(diff[key], tuple):
        return diff[key][0]
    return diff[key]


def get_status(diff, key):
    return diff[key][1]
