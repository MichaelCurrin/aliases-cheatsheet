import json

from prettytable import PrettyTable

from .config import ALIASES_JSON_PATH


json_file_path = ALIASES_JSON_PATH

with open(json_file_path, "r") as file:
    aliase_data = json.load(file)

# Create an instance of PrettyTable
table = PrettyTable()

# In VS Code terminal, the width seems not respected, so set one.
max_width = 60

if not aliase_data:
    print("No data found")
if not isinstance(aliase_data, list):
    print("Data must be a list of dict objects")

column_names = aliase_data[0].keys()
table.field_names = column_names

for column in column_names:
    table.max_width[column] = max_width
    table.align[column] = "l"

for item in aliase_data:
    table.add_row(item.values())

# Print the table
print(table)
