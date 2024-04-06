import os
import re

# Idea
# - List all files and organize by file format
# - Move organized files to your respective folder

download_directory_path = 'C:/Users/mathe/Downloads'

class Setup:
    def __init__(self):
        self.is_file_pattern = r'^[\d\w\s\.\-\+\_\(\)\[\]]+\.[0-9a-z]{2,5}$'

        all_files = self.list_all_downloaded_files()

        print(all_files)

        image_group = []
        exe_group = []
        pdf_group = []
        spreadsheet_group = []
        os_image_group = []
    
    def list_all_downloaded_files(self):
        files_list = []

        with os.scandir(download_directory_path) as entries:
            for entry in entries:
                if re.match(self.is_file_pattern, entry.name):
                    file_name = entry.name
                    files_list.append(file_name)

        return files_list

Setup()