import os
import pandas as pd

def list_sol_filenames_exclude_none(root_folder):
    sol_filenames = set()
    for folder in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder)
        if not os.path.isdir(folder_path) or folder == "None":
            continue
        for file in os.listdir(folder_path):
            if file.endswith('.sol'):
                filename_without_ext = os.path.splitext(file)[0]
                sol_filenames.add(filename_without_ext)
    return sol_filenames

def filter_ground_truth_by_filenames(excel_path, filenames):
    df = pd.read_excel(excel_path)
    filtered_df = df[df['file'].astype(str).isin(filenames)]
    return filtered_df

# === MAIN ===
root_folder = "data/ether frozen (EF)"
excel_path = "ground_truth/ground_truth_EF.xlsx"

# Step 1: Get filenames from versioned folders (excluding "None")
sol_filenames = list_sol_filenames_exclude_none(root_folder)
print(len(sol_filenames))
# Step 2: Filter rows in Excel where file column matches filenames
filtered_df = filter_ground_truth_by_filenames(excel_path, sol_filenames)

# Step 3: Output result (you can also save this)
# print(filtered_df)

# Optional: Save to a new file
filtered_df.to_excel("filtered_ground_truth_EF.xlsx", index=False)
