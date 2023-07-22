all: test

test:
	poetry run pytest tests
.PHONY: test

clean-cache:
	rm tests/cassettes/*
.PHONY: clean-cache

clean-venv:
	rm -rf $(poetry env info -p)
.PHONY: clean-venv

venv:
	poetry install
.PHONY: venv

requirements:
	poetry export --with dev --without-hashes -o requirements-dev.txt
.PHONY: requirements
