SHELL = /bin/bash
APP_DIR = aliases_cheatsheet


run:
	cd $(APP_DIR) && python3 parse_aliases.py

serve:
	cd $(APP_DIR)/www && python3 -m http.server
