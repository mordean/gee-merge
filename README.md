# Google Earth Engine Image Merging/Mosaicking

This tool processes and merges Google Earth Engine (GEE) tiled GeoTiff files efficiently.

## What It Does

1. Extracts zip files from a directory full of unsorted tiled GEE GeoTIFF images.
2. Organizes GeoTIFF files into folders based on common band image names.
3. Merges each band image's GeoTIFF files into one.

## How to Use

Simply update the `source_folder` and `output_folder` paths in `main.py`, then run `main.py` to start the process.