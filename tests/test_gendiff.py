from gendiff.parsers import generate_diff


path_file1 = 'tests/fixtures/before.json'
path_file2 = 'tests/fixtures/after.json'
path_file3 = 'tests/fixtures/before.yaml'
path_file4 = 'tests/fixtures/after.yaml'
correct_answer = open('tests/fixtures/correct_answer').read().rstrip()

def test_generate_diff():
	assert generate_diff(path_file1, path_file2) == correct_answer
	assert generate_diff(path_file3, path_file4) == correct_answer