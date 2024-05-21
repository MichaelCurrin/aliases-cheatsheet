import json
import curses
from prettytable import PrettyTable

from .config import JSON_PATH

json_file_path = JSON_PATH

# Read the JSON file
with open(json_file_path, "r") as file:
    data = json.load(file)


# Function to create a PrettyTable with filtered data
def create_table(data, query, max_width=20):
    table = PrettyTable()
    if data and isinstance(data, list):
        column_names = data[0].keys()
        table.field_names = column_names

        for column in column_names:
            table.max_width[column] = max_width
            table.align[column] = "l"

        for item in data:
            if query.lower() in str(item).lower():
                table.add_row(item.values())

    return table


# Function to run the curses application
def curses_app(stdscr):
    curses.curs_set(1)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    query = ""
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        stdscr.addstr(0, 0, "Filter: " + query[: width - 8])

        table = create_table(data, query, max_width=(width // len(data[0].keys())) - 2)
        table_str = str(table).split("\n")

        for i, line in enumerate(table_str):
            if i + 2 < height:
                stdscr.addstr(i + 2, 0, line[:width])

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_BACKSPACE or key == 127:
            query = query[:-1]
        elif key == 27:  # ESC key to exit
            break
        elif key != -1 and 32 <= key <= 126:  # Only accept printable characters
            query += chr(key)


# Run the curses application
curses.wrapper(curses_app)
