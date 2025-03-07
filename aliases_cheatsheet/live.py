"""
Live view.

Interactive terminal view of your aliases.
"""

import curses
import curses.ascii

from prettytable import PrettyTable

from . import lib
from .config import ALIASES_JSON_PATH


ESCAPE = curses.ascii.ESC

INPUT_TEXT_LABEL = "Filter:"


def is_printable(key: int) -> bool:
    """
    Check if a key code represents a printable character.

    :param key: ASCII key code.

    :returns: True if the key represents a printable character.
    """
    return 32 <= key <= 126


def create_table(table_data: list[dict[str, str]], query: str) -> PrettyTable:
    """
    Create a PrettyTable with filtered data.

    :param table_data: List of dictionaries representing the data.
    :param query: Query string used for filtering.

    :return: PrettyTable object containing filtered data.
    """
    table = PrettyTable()

    if not (table_data and isinstance(table_data, list)):
        print("Warning: No data found to process")
        return table

    column_names = table_data[0].keys()
    table.field_names = column_names

    for column in column_names:
        table.align[column] = "l"

    table.min_width["alias"] = table.max_width["alias"] = 20
    table.min_width["definition"] = table.max_width["definition"] = 50
    table.min_width["comment"] = table.max_width["comment"] = 90

    for item in table_data:
        if query.lower() in str(item).lower():
            table.add_row(item.values())

    return table


def display_table(
    stdscr: curses.window,
    table_str: list[str],
    width: int,
    height: int,
    cursor_pos: int,
    query: str,
) -> None:
    """
    Display the table with headers and content on the screen.

    :param stdscr: Standard screen object provided by curses.
    :param table_str: List of strings representing the table rows.
    :param width: Width of the screen.
    :param height: Height of the screen.
    :param cursor_pos: Current cursor position for scrolling.
    :param query: Current query string for filtering.
    """
    header_lines = 3
    for i in range(header_lines):
        stdscr.addstr(i + 2, 0, table_str[i][:width])

    display_lines = height - 3 - header_lines
    total_height = len(table_str) - header_lines - display_lines
    cursor_pos = max(0, min(cursor_pos, total_height))

    for i in range(display_lines):
        if i + cursor_pos + header_lines < len(table_str):
            value = table_str[i + cursor_pos + header_lines][:width]
            stdscr.addstr(i + 2 + header_lines, 0, value)

    stdscr.move(0, len(f"{INPUT_TEXT_LABEL} {query}"))


def curses_app(stdscr: curses.window) -> None:
    """
    Curses application for real-time filtering and scrolling through data.

    :param stdscr: Standard screen object provided by curses.
    """
    aliases_data = lib.load_json(ALIASES_JSON_PATH)

    curses.curs_set(1)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    query = ""
    cursor_pos = 0
    key = -1

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        stdscr.addstr(0, 0, f"{INPUT_TEXT_LABEL} {query[: width - 8]}")

        current_char = chr(key) if key != -1 else ""
        stdscr.addstr(
            1,
            0,
            f"To exit, press ESC or CTRL+C. DEBUG INFO current key: {key} {current_char}",
        )

        row = aliases_data[0]
        table = create_table(aliases_data, query)
        table_str = str(table).split("\n")

        display_table(stdscr, table_str, width, height, cursor_pos, query)

        stdscr.refresh()

        key = stdscr.getch()

        if key in (curses.KEY_BACKSPACE, 127):
            query = query[:-1]
            cursor_pos = 0
        elif key == ESCAPE:
            break
        elif key == curses.KEY_DOWN:
            cursor_pos = min(cursor_pos + 1, len(table_str) - 3 - 3)
        elif key == curses.KEY_UP:
            cursor_pos = max(cursor_pos - 1, 0)
        elif is_printable(key):
            query += chr(key)
            cursor_pos = 0


if __name__ == "__main__":
    try:
        curses.wrapper(curses_app)
    except KeyboardInterrupt:
        pass
