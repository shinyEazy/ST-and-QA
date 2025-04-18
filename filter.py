import os
import shutil
import pandas as pd
import re

# Load DataFrame
df = pd.read_excel('ground_truth/ground_truth_TP.xlsx')
df['file'] = df['file'].astype(str)

# Source directory
SOURCE_DIR = r"data/timestamp dependency (TP)"

# Recursively find all .sol files and collect their names (without .sol)
sol_file_set = set()
for root, _, files in os.walk(SOURCE_DIR):
    for f in files:
        if f.endswith('.sol'):
            file_name = os.path.splitext(f)[0]
            sol_file_set.add(file_name)

# Filter the DataFrame to keep only rows where 'file' exists in source
filtered_df = df[df['file'].isin(sol_file_set)]
file_names = set(filtered_df['file'])
print(len(file_names))
print(filtered_df)

filtered_df.to_excel('filtered_df.xlsx', index=False)