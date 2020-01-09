from gendiff.scripts.gendiff import generate_diff


path_file1 = 'tests/fixtures/before.json'
path_file2 = 'tests/fixtures/after.json'
correct_answer1 = open('tests/fixtures/correct_answer.json').read().rstrip()
print(correct_answer1)

def test_generate_diff():
	assert generate_diff(path_file1, path_file2) == correct_answer1
