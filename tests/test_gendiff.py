from gendiff import generate_diff
from gendiff.parsers import parse_file
from gendiff.formatters.text import render_text


file1 = parse_file('tests/fixtures/before.json')
file2 = parse_file('tests/fixtures/after.json')
file3 = parse_file('tests/fixtures/before.yaml')
file4 = parse_file('tests/fixtures/after.yaml')
file5 = parse_file('tests/fixtures/before1.json')
file6 = parse_file('tests/fixtures/after1.json')
correct_answer = open('tests/fixtures/correct_answer').read()
correct_answer1 = open('tests/fixtures/correct_answer1').read()

def test_generate_diff():
	assert render_text(generate_diff(file1, file2)) == correct_answer
	assert render_text(generate_diff(file3, file4)) == correct_answer
	assert render_text(generate_diff(file5, file6)) == correct_answer1