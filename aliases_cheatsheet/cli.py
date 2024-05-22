"""
CLI module.

Display and filter custom aliases in the terminal view.
"""

from prettytable import PrettyTable

from . import lib

from .config import ALIASES_JSON_PATH


aliases_data = lib.load_json(ALIASES_JSON_PATH)

# Create an instance of PrettyTable
table = PrettyTable()

# In VS Code terminal, the width seems not respected, so set one.
max_width = 60

if not aliases_data:
    print("No data found")
if not isinstance(aliases_data, list):
    print("Data must be a list of dict objects")

column_names = aliases_data[0].keys()
table.field_names = column_names

for column in column_names:
    table.max_width[column] = max_width
    table.align[column] = "l"

for item in aliases_data:
    table.add_row(item.values())

# Print the table
print(table)
