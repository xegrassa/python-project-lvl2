from gendiff.build_diff import generate_diff
from gendiff.parsers import parse_file
from gendiff.format.text import render_text
from gendiff.format.plain import render_plain
from gendiff.format.json import render_json
import pytest
import os.path


PATH = 'tests/fixtures/'

path_files = [('before.json', 'after.json', 'correct_answer'),
              ('before.yaml', 'after.yaml', 'correct_answer'),
              ('before1.json', 'after1.json', 'correct_answer1')]
path_files1 = [('before1.json', 'after1.json', 'correct_answer_plain_1')]
path_files2 = [('before1.json', 'after1.json', 'correct_answer_json_1')]


def prepare_test(path_file_before,
                 path_file_after,
                 path_file_correct_answer):
  parse_file1 = parse_file(os.path.join(PATH, path_file_before))
  parse_file2 = parse_file(os.path.join(PATH, path_file_after))
  correct_answer = open(os.path.join(PATH, path_file_correct_answer)).read()
  diff = generate_diff(parse_file1, parse_file2)
  return diff, correct_answer


@pytest.mark.parametrize('path_file1, path_file2, path_answer', path_files)
def test_render_text(path_file1, path_file2, path_answer):
  diff, correct_answer = prepare_test(path_file1, path_file2, path_answer)
  assert render_text(diff) == correct_answer


@pytest.mark.parametrize('path_file1, path_file2, path_answer', path_files1)
def test_render_plain(path_file1, path_file2, path_answer):
  diff, correct_answer = prepare_test(path_file1, path_file2, path_answer)
  assert render_plain(diff) == correct_answer


@pytest.mark.parametrize('path_file1, path_file2, path_answer', path_files2)
def test_render_json(path_file1, path_file2, path_answer):
  diff, correct_answer = prepare_test(path_file1, path_file2, path_answer)
  assert render_json(diff) == correct_answer.rstrip()
