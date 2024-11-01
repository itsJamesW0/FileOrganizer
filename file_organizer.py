import os
import shutil
from pathlib import Path

def organize_files(path):
    file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.heif', '.heic', '.raw'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Others': []
}
    for file_name in os.listdir(path):

        file_path = os.path.join(path,file_name)

        if os.path.isdir(file_path):
            continue
        
        if file_name.lower().endswith('.app'):
            app_destination = '/Applications'
            try:
                shutil.move(file_path, os.path.join(app_destination, file_name))
                print(f"Moved {file_name} to {app_destination}")
            except Exception as e:
                print(f"Failed to move {file_name} to {app_destination}: {e}")
            continue  
        
        category = 'Others'

        for key, extension in file_types.items():
            if(Path(file_name).suffix.lower() in extension):
                category = key
                break
        
        category_folder = os.path.join(path,category)
        os.makedirs(category_folder, exist_ok=True)

        try:
            shutil.move(file_path, os.path.join(category_folder, file_name))
            print(f"Moved {file_name} to {category_folder}")
        except Exception as e:
            print(f"Failed to move {file_name}: {e}")

# Please enter the path of the directory you want to organize (e.g., /Users/YourUsername/Downloads):
organize_files("/Users/YourUsername/Downloads")


