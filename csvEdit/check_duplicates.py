import csv
from pathlib import Path
from collections import defaultdict
import os

# Get the downloads folder path
downloads_path = str(Path.home() / "Downloads")
input_file = os.path.join(downloads_path, "NHCC Roster for noGHIN - Sheet1_processed.csv")

# Dictionary to store GHIN numbers and their line numbers
ghin_dict = defaultdict(list)

# Read the CSV and check for duplicates
with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    
    # Skip header row
    next(reader, None)
    
    # Process each row
    for line_num, row in enumerate(reader, start=2):  # start=2 because we skipped header
        if len(row) >= 3:  # Make sure row has at least 3 columns
            ghin = row[2].strip()  # Get GHIN from column C (index 2)
            if ghin:  # Only process non-empty GHIN numbers
                ghin_dict[ghin].append(line_num)

# Check for duplicates and print results
found_duplicates = False
for ghin, line_numbers in ghin_dict.items():
    if len(line_numbers) > 1:
        found_duplicates = True
        print(f"\nDuplicate GHIN number {ghin} found on lines: {', '.join(map(str, line_numbers))}")

if not found_duplicates:
    print("\nNo duplicate GHIN numbers found.") 