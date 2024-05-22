from pathlib import Path


APP_DIR = Path(__file__).parent
DATA_DIR = APP_DIR / "www" / "assets" / "data"

# Output files.
ALIASES_JSON_NAME = "aliases.json"
ALIASES_JSON_PATH = DATA_DIR / ALIASES_JSON_NAME

GIT_ALIASES_JSON_NAME = "git_aliases.json"
GIT_ALIASES_JSON_PATH = DATA_DIR / GIT_ALIASES_JSON_NAME
