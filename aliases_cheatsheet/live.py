"""
Live view.

Interactive terminal view of your aliases.
"""

import curses

from prettytable import PrettyTable

from . import lib
from .config import ALIASES_JSON_PATH


data = lib.load_json(ALIASES_JSON_PATH)


def create_table(
    table_data: list[dict[str, str]], query: str, max_width: int = 20
) -> PrettyTable:
    """
    Create a PrettyTable with filtered data.

    :param table_data: List of dictionaries representing the data.
    :param query: Query string used for filtering.
    :param max_width: Maximum width for each column.

    :return: PrettyTable object containing filtered data.
    """
    table = PrettyTable()

    if not (table_data and isinstance(table_data, list)):
        print("Warning: No data found to process")
        return table

    column_names = table_data[0].keys()
    table.field_names = column_names

    for column in column_names:
        table.max_width[column] = max_width
        table.align[column] = "l"

    for item in table_data:
        if query.lower() in str(item).lower():
            table.add_row(item.values())

    return table


def curses_app(stdscr) -> None:
    """
    Curses application for real-time filtering and scrolling through data.

    :param stdscr: Standard screen object provided by curses.
    """
    curses.curs_set(1)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    query = ""
    cursor_pos = 0  # Initialize cursor position

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        stdscr.addstr(0, 0, "Filter: " + query[: width - 8])

        max_width = width // len(data[0].keys())
        table = create_table(data, query, max_width=(max_width - 2))
        table_str = str(table).split("\n")

        # Display the headers always
        header_lines = 3
        for i in range(header_lines):
            stdscr.addstr(i + 2, 0, table_str[i][:width])

        # Calculate the number of lines that can be displayed for table content
        display_lines = height - 3 - header_lines

        # Ensure cursor position is within valid range
        total_height = len(table_str) - header_lines - display_lines
        cursor_pos = max(0, min(cursor_pos, total_height))

        # Display the table content within the screen bounds, below the headers
        for i in range(display_lines):
            if i + cursor_pos + header_lines < len(table_str):
                value = table_str[i + cursor_pos + header_lines][:width]
                stdscr.addstr(i + 2 + header_lines, 0, value)

        # Move the cursor to the end of the filter input field
        stdscr.move(0, len("Filter: " + query))

        stdscr.refresh()
        key = stdscr.getch()

        if key in (curses.KEY_BACKSPACE, 127):
            query = query[:-1]
            cursor_pos = 0  # Reset cursor when filter changes
        elif key == 27:  # ESC key to exit
            break
        elif key == curses.KEY_DOWN:
            cursor_pos = min(
                cursor_pos + 1, len(table_str) - header_lines - display_lines
            )
        elif key == curses.KEY_UP:
            cursor_pos = max(cursor_pos - 1, 0)
        elif key != -1 and 32 <= key <= 126:  # Only accept printable characters
            query += chr(key)
            cursor_pos = 0  # Reset cursor when filter changes


curses.wrapper(curses_app)
