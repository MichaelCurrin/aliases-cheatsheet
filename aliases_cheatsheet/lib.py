"""
Library module.
"""

import json
from pathlib import Path


def load_json(input_path: Path) -> list[dict]:
    """
    Read a given JSON file and return as an object.
    """
    with open(input_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    return json_data


def save_json(json_data: dict, output_path: Path) -> None:
    """
    Save given data to a JSON file.
    """
    print(f"Writing to: {output_path.name}")

    with output_path.open("w") as json_file:
        json.dump(json_data, json_file, indent=4)
