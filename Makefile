SHELL = /bin/bash
APP_DIR = aliases_cheatsheet

default: install install-dev

install:
	pip install pip --upgrade
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt


fmt:
	black .
	isort .

fmt-check:
	black . --diff --check
	isort . --diff --check-only


cli:
	python3 -m aliases_cheatsheet.cli

cli-scroll:
	python3 -m aliases_cheatsheet.cli | less

live:
	python3 -m aliases_cheatsheet.live

run:
	# TODO check this approach in my template repo
	python3 -m aliases_cheatsheet.parse_aliases

serve:
	cd $(APP_DIR)/www && python3 -m http.server
