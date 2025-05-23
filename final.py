import pandas as pd

# Load both Excel files
df1 = pd.read_excel('filter_ground_truth/filtered_OF.xlsx')
df2 = pd.read_excel('result/integer overflow (OF)/slither.xlsx')

# Ensure file and contract columns are strings for both
df1['file'] = df1['file'].astype(str)
df1['contract'] = df1['contract'].astype(str)

df2['file'] = df2['file'].astype(str)
df2['contract'] = df2['contract'].astype(str)

# Merge df2 into df1 on 'file' and 'contract'
merged_df = pd.merge(df1, df2, on=['file', 'contract'], how='left')

# Fill missing slither values with 0
merged_df['slither'] = merged_df['slither'].fillna(0).astype(int)
# Show result
print(merged_df)
file_names = set(merged_df['file'])
print(len(file_names))
# Optionally save the result
merged_df.to_excel('final.xlsx', index=False)
