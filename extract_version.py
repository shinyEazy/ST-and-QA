import os
import shutil

def get_sol_filenames_without_extension(folder_path):
    sol_files = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.sol'):
                filename_without_ext = os.path.splitext(file)[0]
                sol_files.add(filename_without_ext)
    return sol_files

def filter_lines(output_file_path, keyword, sol_filenames, output_filtered_path):
    matched = []
    with open(output_file_path, 'r', encoding='utf-8') as infile, \
         open(output_filtered_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if keyword not in line:
                continue
            try:
                filename = line.strip().split('\\')[-1].split('.sol')[0]
                version = line.strip().split('\t')[-1]
                if filename in sol_filenames:
                    matched.append((filename, version))
                    outfile.write(line)
            except Exception as e:
                continue
    return matched

def copy_sol_files(source_folder, dest_root_folder, matched_files):
    for filename, version in matched_files:
        src_path = None
        # Search for the file in the folder
        for root, dirs, files in os.walk(source_folder):
            if f"{filename}.sol" in files:
                src_path = os.path.join(root, f"{filename}.sol")
                break

        if src_path:
            dest_dir = os.path.join(dest_root_folder, version)
            os.makedirs(dest_dir, exist_ok=True)
            dest_path = os.path.join(dest_dir, f"{filename}.sol")
            shutil.copy2(src_path, dest_path)
            print(f"✅ Copied {filename}.sol to {dest_dir}")
        else:
            print(f"⚠️ File {filename}.sol not found in source folder!")

# === MAIN ===
source_folder = "Dataset/integer overflow (OF)"
output_txt_path = "output.txt"
filtered_output_path = "filter_output.txt"
dest_folder = "data/integer overflow (OF)"

# Step 1: Get .sol filenames in the source folder
sol_filenames = get_sol_filenames_without_extension(source_folder)

# Step 2: Filter output.txt by filenames and keyword, write to filter_output.txt
matched_files = filter_lines(output_txt_path, "integer overflow (OF)", sol_filenames, filtered_output_path)

# Step 3: Copy files into versioned subfolders
copy_sol_files(source_folder, dest_folder, matched_files)
