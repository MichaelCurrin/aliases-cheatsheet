import json
from pathlib import Path

APP_DIR = Path(__file__).parent
JSON_PATH = APP_DIR / "assets" / "data" / "aliases.json"


def parse_bash_aliases(file_path):
    aliases = []
    with file_path.open("r") as file:
        lines = file.readlines()

    comment_lines = []
    for line in lines:
        line = line.strip()

        if line.startswith("#"):
            comment_lines.append(line[2:])
        elif line.startswith("alias"):
            parts = line.split("=", 1)

            alias_name = parts[0].split()[1]
            alias_definition = parts[1].strip("'")
            comment = "\n".join(comment_lines) if comment_lines else None

            aliases.append(
                {
                    "alias": alias_name,
                    "definition": alias_definition,
                    "comment": comment,
                }
            )
            comment_lines = []
        elif not line:
            # Reset comment lines if there's a blank line
            comment_lines = []

    return aliases


def save_aliases_to_json(aliases, output_file):
    with output_file.open("w") as json_file:
        json.dump(aliases, json_file, indent=4)


def main():
    # TODO make configurable as argument, and check for a few known paths
    # or multiple.
    home_directory = Path.home()

    aliases_file = home_directory / ".aliases"

    aliases = parse_bash_aliases(aliases_file)
    save_aliases_to_json(aliases, JSON_PATH)
    print(f"Aliases have been successfully saved to {JSON_PATH}")


if __name__ == "__main__":
    main()
