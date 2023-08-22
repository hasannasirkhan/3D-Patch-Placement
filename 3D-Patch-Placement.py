import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

# Read the original volume

data = nib.load("original_3D_volume.nii").get_fdata()
desired_output_shape = data.shape

'''

# This area is intentionally left blank.
# You can use your own code to extract the patch and determine its central location.


'''

# I already have extracted patch and its central location through my algorithm.

center_point = (100, 134, 65)
patch_data = nib.load("patch_volume.nii").get_fdata()
patch_size = patch_data.shape

# Create a 3D volume of zeros for patch placement
output_volume = np.zeros(desired_output_shape)

# Calculate patch and output indices
patch_start = np.array(center_point) - np.array(patch_size) // 2
patch_end = patch_start + np.array(patch_size)
output_start = np.maximum(patch_start, 0)
output_end = np.minimum(patch_end, desired_output_shape)

# Place the patch data into the output volume
output_volume[output_start[0]:output_end[0], output_start[1]:output_end[1], output_start[2]:output_end[2]] = \
patch_data[output_start[0] - patch_start[0]:output_end[0] - patch_start[0],
            output_start[1] - patch_start[1]:output_end[1] - patch_start[1],
            output_start[2] - patch_start[2]:output_end[2] - patch_start[2]]

# Crop the output volume to the desired shape
output_volume_cropped = output_volume[:desired_output_shape[0], :desired_output_shape[1], :desired_output_shape[2]]
