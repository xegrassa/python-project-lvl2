import json
import yaml


def is_json(path_file):
	if path_file[path_file.rfind('.'):] == '.json': return True
	return False

def parse_file(path_file, is_json):
	if is_json: return json.load(open(path_file))
	return yaml.safe_load(open(path_file))

def gen_key(key, operator=' '):
	return "    {} {}: {}\n".format(operator, key[0], key[1])

def generate_diff(path_to_file1, path_to_file2):
    file1 = parse_file(path_to_file1, is_json(path_to_file1))
    file2 = parse_file(path_to_file2, is_json(path_to_file2))
    set_no_change = (set(file1.items()) &
                     set(file2.items()))
    set_adding = {(i, file2[i]) for i in (set(file2.keys()) -
                                          set(file1.keys()))}
    set_deleting = {(i, file1[i]) for i in (set(file1.keys()) -
                                            set(file2.keys()))}
    set_changing = (set(file1) & set(file2)) - set(dict(set_no_change).keys())
    diff = "{\n"
    for i in set_no_change:
    	diff += gen_key(i)
    for i in set_adding:
    	diff += gen_key(i, '+')
    for i in set_changing:
        diff += "    - {}: {}\n".format(i, file1[i])
        diff += "    + {}: {}\n".format(i, file2[i])
    for i in set_deleting:
    	diff += gen_key(i, '-')
    diff += "}"
    return diff