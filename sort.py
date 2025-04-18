import os
import shutil
import pandas as pd
import re

# Load DataFrame
df = pd.read_excel('ground_truth/ground_truth_TP.xlsx')
df['file'] = df['file'].astype(str)

# Source and destination directories
SOURCE_DIR = r"Dataset/timestamp dependency (TP)"
DEST_DIR = r"data/timestamp dependency (TP)"

os.makedirs(DEST_DIR, exist_ok=True)

# Get set of .sol filenames (without extension) in source dir
sol_file_set = {
    os.path.splitext(f)[0]
    for f in os.listdir(SOURCE_DIR)
    if f.endswith('.sol')
}

# Filter the DataFrame to keep only rows where 'file' exists in source
filtered_df = df[df['file'].isin(sol_file_set)]
file_names = set(filtered_df['file'])

print(filtered_df)

# Copy files that are in file_names
# for filename in os.listdir(SOURCE_DIR):
#     if filename.endswith('.sol'):
#         file_id = os.path.splitext(filename)[0]
#         if file_id in file_names:
#             src_path = os.path.join(SOURCE_DIR, filename)
#             dest_path = os.path.join(DEST_DIR, filename)
#             shutil.copyfile(src_path, dest_path)
#             print(f"Copied: {filename}")
#         else:
#             print(f"Skipped: {filename}")

# print("Copying complete.")

# # Regex to extract solidity version
# VERSION_REGEX = re.compile(r'pragma\s+solidity\s+[^0-9]*([0-9]+\.[0-9]+\.[0-9]+)')

# # Now work on files in the destination directory
# for filename in os.listdir(DEST_DIR):
#     if not filename.endswith(".sol"):
#         continue

#     full_path = os.path.join(DEST_DIR, filename)

#     try:
#         with open(full_path, 'r', encoding='utf-8') as f:
#             content = f.read()
#     except Exception as e:
#         print(f"Could not read {filename}: {e}")
#         continue

#     match = VERSION_REGEX.search(content)
#     if match:
#         version = match.group(1)
#     else:
#         version = "rest"  # fallback folder if version is missing
#         print(f"No version found in {filename}, placing in 'rest'.")

#     # Create version folder inside DEST_DIR
#     version_folder = os.path.join(DEST_DIR, version)
#     os.makedirs(version_folder, exist_ok=True)

#     # Move the file into its versioned folder
#     new_path = os.path.join(version_folder, filename)
#     shutil.move(full_path, new_path)

#     print(f"Moved {filename} to {version_folder}")