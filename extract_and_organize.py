import os
import zipfile
import shutil

def process_zip_files(source_folder, folder_names_to_create):
    for folder_name in folder_names_to_create:
        folder_path = os.path.join(source_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    for item in os.listdir(source_folder):
        item_path = os.path.join(source_folder, item)

        if os.path.isfile(item_path) and item.lower().endswith('.zip'):
            unzip_and_move(item_path, source_folder)
            os.remove(item_path)

def organize_files(source_folder, folder_names_to_create):
    move_files_from_nested_folders(source_folder, source_folder)

    for folder_name in folder_names_to_create:
        for item in os.listdir(source_folder):
            item_path = os.path.join(source_folder, item)
            if os.path.isfile(item_path) and item.lower().endswith('.tif') and folder_name.replace("_Non_Merged", "") in item:
                destination_folder = os.path.join(source_folder, folder_name)
                shutil.move(item_path, os.path.join(destination_folder, item))

def unzip_and_move(zip_folder, destination_folder):
    with zipfile.ZipFile(zip_folder, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

    extracted_folders = [item for item in os.listdir(destination_folder) if os.path.isdir(os.path.join(destination_folder, item))]
    folder_counts = {}

    for folder_name in extracted_folders:
        base_folder_name = folder_name
        count = 1

        while folder_name in folder_counts:
            folder_name = f"{base_folder_name}_{count}"
            count += 1

        folder_counts[folder_name] = 1

        if folder_name != base_folder_name:
            old_path = os.path.join(destination_folder, base_folder_name)
            new_path = os.path.join(destination_folder, folder_name)
            os.rename(old_path, new_path)

    return extracted_folders

def move_contents(source_folder, destination_folder):
    for item in os.listdir(source_folder):
        item_path = os.path.join(source_folder, item)
        if os.path.isfile(item_path):
            shutil.move(item_path, os.path.join(destination_folder, item))

def move_files_from_nested_folders(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            shutil.move(file_path, os.path.join(destination_folder, file))

def delete_empty_folders(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)