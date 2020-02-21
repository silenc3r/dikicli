all: test

test:
	pipenv run pytest tests
.PHONY: test

upload:
	rm -rf dist
	pipenv run python setup.py sdist bdist_wheel --universal
	pipenv run twine upload dist/*
.PHONY: upload
