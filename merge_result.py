import os
import pandas as pd

# Directory containing your Excel files
RESULT_DIR = r'result/timestamp dependency (TP)'

# Collect all Excel files in the directory
excel_files = [
    os.path.join(RESULT_DIR, f)
    for f in os.listdir(RESULT_DIR)
    if f.endswith('.xlsx')
]

# Read and merge all files
all_dfs = []
for file in excel_files:
    df = pd.read_excel(file)
    all_dfs.append(df)

# Combine into one DataFrame and drop duplicates
merged_df = pd.concat(all_dfs, ignore_index=True)
merged_df = merged_df.drop_duplicates()
merged_df = merged_df.sort_values(by='file', ascending=True)


file_names = set(merged_df['file'])
# print(len(file_names))
# Show result
print(merged_df)

# Optionally save the merged result
merged_df.to_excel('merged_result.xlsx', index=False)
