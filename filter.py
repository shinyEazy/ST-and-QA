import os
import shutil
import pandas as pd
import re

# Load DataFrame
df = pd.read_excel('ground_truth/ground_truth_OF.xlsx')
df['file'] = df['file'].astype(str)

# Source directory
SOURCE_DIR = r"Dataset/integer overflow (OF)"

# Recursively find all .sol files, but skip ones under "None" subfolder
sol_file_set = set()
for root, _, files in os.walk(SOURCE_DIR):
    if os.path.basename(root) == "None":
        continue  # Skip the "None" folder
    for f in files:
        if f.endswith('.sol'):
            file_name = os.path.splitext(f)[0]
            sol_file_set.add(file_name)

# Filter the DataFrame to keep only rows where 'file' exists in valid .sol set
filtered_df = df[df['file'].isin(sol_file_set)]
file_names = set(filtered_df['file'])

print(len(file_names))
# print(filtered_df)

# Save filtered DataFrame
filtered_df.to_excel('filtered_OF.xlsx', index=False)
