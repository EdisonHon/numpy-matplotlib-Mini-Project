# Edison Hon
# 04/06/2025
# numpy/matplotlib Mini-project step 11: generates a seating chart for a classroom

import numpy as np
from numpy import random

# Get classroom size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of chairs per row: "))
total_seats = rows * cols

# Define names: AAA to ZZZ
names = [chr(i)*3 for i in range(ord('A'), ord('Z') + 1)]  # ['AAA', 'BBB', ..., 'ZZZ']

# Check if enough names are available
if total_seats > len(names):
    print("Not enough names (only 26). Please use a smaller classroom size.")
    exit()

# Randomly assign names
selected_names = random.choice(names, size=total_seats, replace=False)

# Reshape into 2D array
seating_chart = selected_names.reshape((rows, cols))

# Determine column width (based on longest name)
name_col_width = max(len(name) for name in selected_names) + 4 #extra padding
pos_col_width =7

# Print as formatted table
print("\nClassroom Seating Chart:\n")
for i in range(rows):
    name_row = ""
    pos_row = ""
    for j in range(cols):
        name = seating_chart[i][j]
        position = f"({i},{j})"
        name_row += name.center(name_col_width)
        pos_row += position.center(pos_col_width)
    print(name_row)
    print(pos_row)
