#makefile
install:
	poetry install 
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest --cov=tests
instgendiff:
	pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ egrassa-gendiff
del:
	pip uninstall -y egrassa-gendiff
#pip uninstall -y prompt
