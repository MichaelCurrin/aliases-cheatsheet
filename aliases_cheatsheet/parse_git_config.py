"""
Parse Git aliases from .gitconfig file.
"""

import configparser
from pathlib import Path

from . import lib
from .config import GIT_ALIASES_JSON_PATH


def parse_git_aliases(file_path: Path) -> list[dict]:
    """
    Parse Git aliases from `.gitconfig` file.

    :param file_path: Path to the `.gitconfig` file.

    :return: Parsed aliases.
    """

    config = configparser.ConfigParser(allow_no_value=True, interpolation=None)
    config.read(file_path)

    if "alias" not in config:
        print("Warning: could not find 'alias' field in Git config.")
        return []

    aliases = []

    for alias, value in config["alias"].items():
        if value is None:
            continue

        alias_definition = value.strip().strip('"')
        # Not supported by configparser to find comments.
        comment = ""

        item = {"alias": alias, "definition": alias_definition, "comment": comment}
        aliases.append(item)

    return aliases


def main():
    home_directory = Path.home()
    gitconfig_file = home_directory / ".gitconfig"

    aliases = parse_git_aliases(gitconfig_file)
    lib.save_json(aliases, GIT_ALIASES_JSON_PATH)


if __name__ == "__main__":
    main()
