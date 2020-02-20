from gendiff.format.json import render_json as json
from gendiff.format.text import render_text as text
from gendiff.format.plain import render_plain as plain
import argparse


JSON = 'json'
TEXT = 'text'
PLAIN = 'plain'


def get_render(arg):
    if arg == TEXT:
        return text
    if arg == JSON:
        return json
    if arg == PLAIN:
        return plain
    msg = ("invalid choice: '{}' (choose from 'text', 'json', 'plain')".
           format(arg))
    raise argparse.ArgumentTypeError(msg)
