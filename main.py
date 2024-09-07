import os
from extract_and_organize import process_zip_files, organize_files, delete_empty_folders
from merge_rasters import merge_rasters

# ============================= USER INPUT =============================

# Source folder is where all exported GEE band image data are stored
source_folder = r"C:\Users\Edit\Input"

# Output folder is where merged/mosaicked rasters are written
output_folder = r"C:\Users\Edit\Output"

# The string format is the base image name (without extra text GEE export adds to split datasets) + "_Non_Merged".
# Example: If GEE exports multiple parts of "Copernicus_DEM" as "Copernicus_DEM_1", "Copernicus_DEM_2", etc., 
#   you only need the base name "Copernicus_DEM" followed by "_Non_Merged".
folder_names_to_create = [
    "Copernicus_DEM_Non_Merged",
    "L8_B2_Non_Merged"]

# ============================= END OF USER INPUT =============================

# Check if source folder exists
if not os.path.exists(source_folder):
    raise FileNotFoundError(f"Source folder '{source_folder}' does not exist!")

# Step 1: Process zip files and organize into folders
print("Starting zip file extraction and organization...")
process_zip_files(source_folder, folder_names_to_create)

# Step 2: Organize GeoTIFF files into appropriate folders
print("Organizing GeoTIFF files into corresponding folders...")
organize_files(source_folder, folder_names_to_create)

# Step 3: Delete empty folders
print("Deleting empty folders...")
delete_empty_folders(source_folder)

# Step 4: Merge raster files
print("Starting raster merging process...")
merge_rasters(input_root_folder=source_folder, output_root_folder=output_folder)

print("Processing complete!")