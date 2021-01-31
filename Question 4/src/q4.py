# %%
import cv2
import numpy as np

# %%
# Read data
with open('../input/input_question_4', 'r') as f:
    data = f.read()
    
# Transform str data to float data
bin_data = []
for row in data.split('\n')[:-1]:
    bin_data.append([float(p) for p in row.split()])
    
# Transform float data to uint8
bin_data = np.array(bin_data)
bin_data = bin_data.astype(np.uint8)

# Use cv connectedComponents
um_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
            bin_data, connectivity=8)

# Write to file
with open('../output/output_question_4', 'w') as f:
    for label in labels:
        for p in label:
            f.write(str(p) + '\t')
        f.write('\n')
# %%
