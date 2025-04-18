import pandas as pd

# Load the merged DataFrame
df = pd.read_excel('merged_filtered_slither.xlsx')

# Clean 'ground truth' column (convert things like '0->1' to '1', etc.)
df['ground truth'] = df['ground truth'].astype(str)
df['ground truth'] = df['ground truth'].str.extract(r'(\d)').fillna('0').astype(int)

# Ensure slither is also int
df['slither'] = df['slither'].astype(int)

# Calculate confusion matrix components
tp = len(df[(df['slither'] == 1) & (df['ground truth'] == 1)])
fp = len(df[(df['slither'] == 1) & (df['ground truth'] == 0)])
fn = len(df[(df['slither'] == 0) & (df['ground truth'] == 1)])
tn = len(df[(df['slither'] == 0) & (df['ground truth'] == 0)])

# Precision, Recall, Accuracy, F1
precision = tp / (tp + fp) if (tp + fp) else 0
recall = tp / (tp + fn) if (tp + fn) else 0
acc = (tp + tn) / (tp + tn + fp + fn)
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

# Print metrics
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"ACC:       {acc:.4f}")
print(f"F1:        {f1:.4f}")
