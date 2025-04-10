import json
import os
import pandas as pd

df = pd.read_excel('aa.xlsx')
# print(df)

def get_filename(file_id):
    return f"{file_id}.sol"

ground_truth = {}
for index, row in df.iterrows():
    file_id = row['file']             
    contract_name = row['contract']   
    reentrancy_label = int(row['ground truth']) 
    filename = get_filename(file_id)  
    ground_truth[(filename, contract_name)] = reentrancy_label

all_contracts = set(ground_truth.keys()) 
vulnerable = {contract for contract, label in ground_truth.items() if label == 1}

with open('all_findings.json', 'r') as f:
    slither_data = json.load(f)

detected = set()
for detector in slither_data['results']['detectors']:
    if 'reentrancy' in detector['check']: 
        for element in detector['elements']:
            if 'type_specific_fields' in element and 'parent' in element['type_specific_fields']:
                parent = element['type_specific_fields']['parent']
                if parent['type'] == 'contract':
                    contract_name = parent['name']
                    filename = element['source_mapping']['filename_relative']
                    detected.add((filename, contract_name))
                else:
                    # print(f"Warning: Parent is not a contract for element: {element}")
                    pass
            else:
                # print(f"Warning: Missing 'type_specific_fields' or 'parent' in element: {element}")
                pass

detected = detected & all_contracts

print(all_contracts)

TP = detected & vulnerable       
FP = detected - vulnerable          
FN = vulnerable - detected          
TN = all_contracts - (detected | vulnerable)  

tp_count = len(TP)
fp_count = len(FP)
fn_count = len(FN)
tn_count = len(TN)

total_predictions = tp_count + fp_count
total_vulnerable = tp_count + fn_count
total_contracts = len(all_contracts)

precision = tp_count / total_predictions if total_predictions > 0 else 0
recall = tp_count / total_vulnerable if total_vulnerable > 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
accuracy = (tp_count + tn_count) / total_contracts if total_contracts > 0 else 0

print(f"True Positives (TP): {tp_count}")
print(f"False Positives (FP): {fp_count}")
print(f"True Negatives (TN): {tn_count}")
print(f"False Negatives (FN): {fn_count}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"Accuracy: {accuracy:.4f}")