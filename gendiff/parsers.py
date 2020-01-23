import json
import yaml
import os.path


JSON = '.json'


def parse_file(path_file):
    is_json = os.path.splitext(path_file)[1] == JSON
    loader = json.load if is_json else yaml.safe_load
    return loader(open(path_file))
