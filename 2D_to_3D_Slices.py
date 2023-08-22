
import numpy as np
import os
import nibabel as nib

# Folder containing the 2D numpy arrays
folder_path = 'patient1_mask'

# Dictionary to store patient IDs and their corresponding slices
patient_slices = {}

# Iterate through the files in the folder
for file_name in os.listdir(folder_path):
    if file_name.startswith("mask_") and file_name.endswith(".npy"):
        #print("File Name: ", file_name)
        # Parse patient ID and slice number from the file name
        _, patient_id, slice_number = file_name.split("_")
        #print("Patient_id: ", patient_id)
        #print("Slice_id: ", slice_number)
        slice_number = int(slice_number.replace(".npy", ""))
        #print("Slice_Number: ", slice_number)
        
        # Load the 2D numpy array
        slice_data = np.load(os.path.join(folder_path, file_name))
        #print("Shape of the slice: ", slice_data.shape)
        # Add the slice data to the corresponding patient's dictionary entry
        if patient_id not in patient_slices:
            patient_slices[patient_id] = {}
        patient_slices[patient_id][slice_number] = slice_data

# Create 3D volumes for each patient
for patient_id, slices in patient_slices.items():
    
    print("patient_id: ", patient_id)
    print("slices: ", slices)
    
    # Determine the maximum slice number for this patient
    #max_slice_number = max(slices.keys())
    
    # Initialize the new volume for this patient
    new_volume = np.zeros((128, 128, 128), dtype=np.float32)
    
    # Fill the volume with slice data for this patient
    for slice_number, slice_data in slices.items():
        new_volume[:, :, slice_number] = slice_data
        
    '''    
    # Create the larger volume (240, 240, 155) and place the smaller volume at the center
    new_volume_large = np.zeros((240, 240, 155), dtype=np.float32)
    
    # Calculate the center position to place the smaller volume
    center_x = (240 - 128) // 2
    center_y = (240 - 128) // 2
    center_z = (155 - 128) // 2
    
    # Place the smaller volume in the center of the larger volume
    new_volume_large[center_x:center_x+128, center_y:center_y+128, center_z:center_z+128] = new_volume
  
    '''
    nifti_img = nib.Nifti1Image(new_volume, affine=np.eye(4))  # Assuming identity affine

    # Save the new volume for this patient
    volume_name = f"patient_{patient_id}.nii.gz"
    nib.save(nifti_img, volume_name)

print("New volumes created.")

