#makefile
install:
	poetry install 
lint:
	poetry run flake8 gendiff
test:
#	python -m pytest --cov=tests
	poetry run pytest --cov=tests
instgendiff:
	pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ egrassa-gendiff
del:
	pip uninstall -y egrassa-gendiff
push:
	git add -A
	git commit -m "auto commit"
	git push
