"""
Parse aliases module.
"""

from pathlib import Path

from . import lib
from .config import ALIASES_JSON_PATH


def parse_bash_aliases(file_path: Path):
    with file_path.open("r") as file:
        lines = file.readlines()

    aliases = []
    comment_lines = []

    for line in lines:
        line = line.strip()

        if line.startswith("#"):
            comment_lines.append(line[2:])
        elif line.startswith("alias"):
            parts = line.split("=", 1)

            alias_name = parts[0].split()[1]
            alias_definition = parts[1].strip("'")
            comment = "\n".join(comment_lines) if comment_lines else ""

            item = {
                "alias": alias_name,
                "definition": alias_definition,
                "comment": comment,
            }
            aliases.append(item)

            comment_lines = []
        elif not line:
            # Reset comment lines if there's a blank line
            comment_lines = []

    return aliases


def main():
    home_directory = Path.home()

    aliases_file = home_directory / ".aliases"

    aliases = parse_bash_aliases(aliases_file)
    lib.save_json(aliases, ALIASES_JSON_PATH)


if __name__ == "__main__":
    main()
