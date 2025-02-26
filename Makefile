SHELL = /bin/bash
APP_DIR = aliases_cheatsheet

default: install

all: hooks install typecheck


install:
	poetry install

upgrade:
	poetry update


fix:
	poetry run ruff check --fix
	poetry run ruff format

typecheck:
	poetry run mypy $(APP_DIR)


parse:
	# TODO check this approach in my template repo
	poetry run python -m aliases_cheatsheet.parse_aliases
	poetry run python -m aliases_cheatsheet.parse_git_config

cli:
	poetry run python -m aliases_cheatsheet.cli

cli-scroll:
	poetry run python -m aliases_cheatsheet.cli | less

live:
	poetry run python -m aliases_cheatsheet.live


s serve:
	cd $(APP_DIR)/www && python3 -m http.server
