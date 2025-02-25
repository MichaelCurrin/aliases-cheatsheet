"""
CLI module.

Display and filter custom aliases in the terminal view.
"""

from prettytable import PrettyTable

from . import lib
from .config import ALIASES_JSON_PATH


def display(aliases_data: list[dict], max_width: int = 60) -> None:
    """
    Display input data as a table.
    """
    if not aliases_data:
        print("No data found")
        return

    if not isinstance(aliases_data, list):
        print("Data must be a list of dict objects")
        return

    table = PrettyTable()

    column_names = aliases_data[0].keys()
    table.field_names = column_names

    for column in column_names:
        table.max_width[column] = max_width
        table.align[column] = "l"

    for item in aliases_data:
        table.add_row(item.values())

    print(table)


def main() -> None:
    """
    Main command-line entry-point.
    """
    aliases_data = lib.load_json(ALIASES_JSON_PATH)
    display(aliases_data)


if __name__ == "__main__":
    main()
