import csv
import os
from pathlib import Path

# Get the downloads folder path
downloads_path = str(Path.home() / "Downloads")
input_file = os.path.join(downloads_path, "NHCC Roster for noGHIN - Sheet1.csv")
output_file = os.path.join(downloads_path, "NHCC Roster for noGHIN - Sheet1_processed.csv")

# Read the input CSV and process it
with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Process each row
    for row in reader:
        if not row:  # Skip empty rows
            continue
            
        # Get the first column value
        first_col = row[0]
        
        # Split at first space
        parts = first_col.split(' ', 1)
        
        # Create new row with split values
        new_row = [parts[0]]  # First part goes to first column
        if len(parts) > 1:
            new_row.append(parts[1])  # Second part goes to second column
        else:
            new_row.append('')  # Empty string if no second part
            
        # Add any remaining columns from original row
        new_row.extend(row[1:])
        
        # Write the new row
        writer.writerow(new_row)

print(f"Processing complete. Output saved to: {output_file}") 