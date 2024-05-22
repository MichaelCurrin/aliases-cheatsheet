"""
Library module.
"""

import json
from pathlib import Path


def save_aliases_to_json(aliases: dict, output_file: Path) -> None:
    """
    Save parsed aliases to a JSON file.

    :param aliases: Parsed aliases.
    :param output_file: Path to the output JSON file.
    """
    print(f"Writing to: {output_file.name}")

    with output_file.open("w") as json_file:
        json.dump(aliases, json_file, indent=4)
