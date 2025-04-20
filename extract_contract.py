import json
import pandas as pd
import os

# Load JSON result (from a file or string)
with open('all_findings.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Prepare data list
records = []

# Traverse detectors
for detector in data.get('results', {}).get('detectors', []):
    for element in detector.get('elements', []):
        # Only interested in functions
        if element.get('type') == 'function':
            file_path = element['source_mapping'].get('filename_short')  # e.g., 1318.sol
            contract_info = element.get('type_specific_fields', {}).get('parent', {})
            contract_name = contract_info.get('name', '')

            if file_path and contract_name:
                file_name_no_ext = os.path.splitext(file_path)[0]  # e.g., "1318"
                records.append({
                    'file': file_name_no_ext,
                    'contract': contract_name,
                    'slither': 1
                })

# Convert to DataFrame
df = pd.DataFrame(records)
df = df.drop_duplicates()

# Show result
print(df)

# Optionally save
df.to_excel('result/integer overflow (OF)/slither_extracted_0426.xlsx', index=False)
