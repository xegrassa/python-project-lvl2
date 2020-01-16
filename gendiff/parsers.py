import json
import yaml


def is_json(path_file):
    if path_file[path_file.rfind('.'):] == '.json':
        return True
    return False


def parse_file(path_file):
    if is_json(path_file):
        return json.load(open(path_file))
    return yaml.safe_load(open(path_file))
