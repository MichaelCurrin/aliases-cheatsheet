import curses
import json

from prettytable import PrettyTable

from .config import JSON_PATH


json_file_path = JSON_PATH


# TODO add text like about, and ESC to exit
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
    cursor_pos = 0  # Initialize cursor position
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        stdscr.addstr(0, 0, "Filter: " + query[: width - 8])

        table = create_table(data, query, max_width=(width // len(data[0].keys())) - 2)
        table_str = str(table).split("\n")

        # Display the headers always
        header_lines = 3
        for i in range(header_lines):
            stdscr.addstr(i + 2, 0, table_str[i][:width])

        # Calculate the number of lines that can be displayed for table content
        display_lines = height - 3 - header_lines

        # Ensure cursor position is within valid range
        cursor_pos = max(
            0, min(cursor_pos, len(table_str) - header_lines - display_lines)
        )

        # Display the table content within the screen bounds, below the headers
        for i in range(display_lines):
            if i + cursor_pos + header_lines < len(table_str):
                stdscr.addstr(
                    i + 2 + header_lines,
                    0,
                    table_str[i + cursor_pos + header_lines][:width],
                )

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_BACKSPACE or key == 127:
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


# Run the curses application
curses.wrapper(curses_app)
