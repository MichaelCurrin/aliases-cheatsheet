"""
Library module.
"""

import json
from pathlib import Path


def load_json(json_file_path: Path):
    with open(json_file_path, "r") as file:
        data = json.load(file)

    return data


def save_aliases_to_json(aliases: dict, output_file: Path) -> None:
    """
    Save parsed aliases to a JSON file.

    :param aliases: Parsed aliases.
    :param output_file: Path to the output JSON file.
    """
    print(f"Writing to: {output_file.name}")

    with output_file.open("w") as json_file:
        json.dump(aliases, json_file, indent=4)
