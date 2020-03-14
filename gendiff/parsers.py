import json
import yaml
import os.path


JSON = '.json'
YAML = '.yaml'


def parse_file(path_file):
    is_json = os.path.splitext(path_file)[1] == JSON
    is_yaml = os.path.splitext(path_file)[1] == YAML
    if is_json:
        loader = json.load
    elif is_yaml:
        loader = yaml.safe_load
    else:
        raise Warning
    return loader(open(path_file))
