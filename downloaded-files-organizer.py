import os
import re

# Idea
# - List all files
# - Organize by file format
# - Move organized files to your respective folder

download_directory_path = 'C:/Users/mathe/Downloads'

class Setup:

    def __init__(self):

        self.is_file_pattern = r'^[\d\w\s\.\-\+\_\(\)\[\]]+\.[0-9a-z]{2,5}$'

        self.all_files = self.list_all_downloaded_files()

        self.pdf_pattern = self.create_file_format_pattern('pdf')
        self.jpeg_pattern = self.create_file_format_pattern('jpeg')
        self.jpg_pattern = self.create_file_format_pattern('jpg')
        self.png_pattern = self.create_file_format_pattern('png')
        self.svg_pattern = self.create_file_format_pattern('svg')
        self.exe_pattern = self.create_file_format_pattern('exe')
        self.xlsx_pattern = self.create_file_format_pattern('xlsx')
        self.pptx_pattern = self.create_file_format_pattern('pptx')
        self.iso_pattern = self.create_file_format_pattern('iso')
        self.part_pattern = self.create_file_format_pattern('part')
        self.zip_pattern = self.create_file_format_pattern('zip')
        self.seven_zip_pattern = self.create_file_format_pattern('7z')

        self.image_group = []
        self.exe_group = []
        self.pdf_group = []
        self.spreadsheet_group = []
        self.os_image_group = []
        self.slides_group = []
        self.compacted_group = []

        for file in self.all_files:
            if re.match(self.pdf_pattern, file):
                self.pdf_group.append(file)
                self.all_files.remove(file)
                
        print(self.pdf_group)
        print(self.all_files)

    
    def list_all_downloaded_files(self):
        files_list = []

        with os.scandir(download_directory_path) as entries:
            for entry in entries:
                if re.match(self.is_file_pattern, entry.name):
                    file_name = entry.name
                    files_list.append(file_name)

        return files_list
    

    def create_file_format_pattern(self, format_name):
        return fr'^[\d\w\s\.\-\+\_\(\)\[\]]+\.{format_name}$'



Setup()