# Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from their current location to a new folder.

import os, shutil
from pathlib import Path

specified_folder_tree = input("Enter a folder tree to walk for selective copying based on the .jpg extension: ")

h = Path.home()

(h / Path(f'{specified_folder_tree}_duplicated_jpg_files')).mkdir(exist_ok=True)

d = h / f"{specified_folder_tree}_duplicated_jpg_files"

for folder_name, subfolders, filenames in os.walk(h / specified_folder_tree):
    for filename in filenames:
        p = Path(folder_name)
        p_stem = Path(filename).stem
        p_suffix = Path(filename).suffix
        src = p / filename
        is_jpg = src.is_file() and src.suffix.lower() in {".jpg", ".jpeg"}
        if is_jpg:
            print(p, filename)
            #shutil.copy(src, d / f"{p_stem}_duplicate{p_suffix}")
