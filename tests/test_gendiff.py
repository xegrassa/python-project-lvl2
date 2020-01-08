from gendiff import generate_diff


path_file1 = 'fixtures/before.json'
path_file2 = 'fixtures/after.json'
correct_answer1 = open('fixtures/correct_answer.json','r').read()
print(correct_answer1)

def test_generate_diff():
	assert generate_diff(path_file1, path_file2) == correct_answer1.rstrip()
