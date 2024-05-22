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

pretty:
	npx prettier -w assets/{js,css} index.html


parse:
	# TODO check this approach in my template repo
	python -m aliases_cheatsheet.parse_aliases
	python -m aliases_cheatsheet.parse_git_config

cli:
	python -m aliases_cheatsheet.cli

cli-scroll:
	python -m aliases_cheatsheet.cli | less

live:
	python -m aliases_cheatsheet.live


serve:
	cd $(APP_DIR)/www && python -m http.server
