import os
import rioxarray as riox
from rioxarray.merge import merge_arrays

def merge_rasters(input_root_folder, output_root_folder):
    nested_folders = [folder for folder in os.listdir(input_root_folder) if os.path.isdir(os.path.join(input_root_folder, folder))]

    for folder_name in nested_folders:
        input_folder = os.path.join(input_root_folder, folder_name)
        print(f"Processing rasters in: {input_folder}")

        raster_files = [file for file in os.listdir(input_folder) if file.endswith(".tif")]
        raster_dataarrays = [riox.open_rasterio(os.path.join(input_folder, file)) for file in raster_files]

        merged_raster = merge_arrays(dataarrays=raster_dataarrays, nodata=0)
        folder_name = folder_name.replace("Non_Merged", "Merged")
        output_file = os.path.join(output_root_folder, folder_name + ".tif")

        merged_raster.rio.set_crs(raster_dataarrays[0].rio.crs)
        merged_raster.rio.set_spatial_dims(x_dim='x', y_dim='y')
        merged_raster.rio.to_raster(output_file, driver='GTiff')

        print(f"File written to: {output_file}")
