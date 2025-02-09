.DEFAULT_GOAL := build

test: .venv
	.venv/bin/pytest tests
.PHONY: test

build: .venv
	.venv/bin/python3 setup.py sdist bdist_wheel
.PHONY: build

update-dependencies: .venv
	# install most recent versions of dependencies
	.venv/bin/pip install -e .[dev]
	$(MAKE) requirements-dev
	$(MAKE) rm-venv
	$(MAKE) venv
.PHONY: update-dependencies

requirements-dev: .venv
	./run.sh pip --require-virtualenv freeze --exclude-editable 2>/dev/null | tee requirements-dev.txt
.PHONY: requirements-dev

venv: .venv
.PHONY: venv

.venv:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements-dev.txt
	.venv/bin/pip install wheel

rm-venv:
	rm -rf .venv/
.PHONY: clean-venv

clean:
	rm -rf .venv/
	rm -rf dist/
.PHONY: clean
