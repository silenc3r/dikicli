all: test

test:
	poetry run pytest tests
.PHONY: test

clean:
	rm tests/cassettes/*
.PHONY: clean
