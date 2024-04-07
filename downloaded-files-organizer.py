import os
import re

# Idea
# - List all files
# - Organize by file format
# - Move organized files to your respective folder

download_directory_path = 'C:/Users/mathe/Downloads'

def create_file_format_pattern(format_name):
    return fr'^[\d\w\s\.\-\+\_\(\)\[\]]+\.{format_name}$'

class Setup:

    def __init__(self):

        self.is_file_pattern = r'^[\d\w\s\.\-\+\_\(\)\[\]]+\.[0-9a-z]{2,5}$'

        self.all_files = self.list_all_downloaded_files()

        self.exe_pattern = create_file_format_pattern('exe')
        self.xlsx_pattern = create_file_format_pattern('xlsx')
        self.pptx_pattern = create_file_format_pattern('pptx')
        self.iso_pattern = create_file_format_pattern('iso')
        self.part_pattern = create_file_format_pattern('part')
        self.zip_pattern = create_file_format_pattern('zip')
        self.seven_zip_pattern = create_file_format_pattern('7z')

        self.spreadsheet_group = []
        self.os_image_group = []
        self.slides_group = []
        self.compacted_group = []

        self.file_groups = [
            PdfGroup(),
            ImageGroup(),
            ExecutableGroup()
        ]

        for file in self.all_files:
            for file_group in self.file_groups:
                file_group.filter_file(file)

            self.all_files.remove(file)
                
        for file_group in self.file_groups:
            print(f'\n-----  {file_group.folder_group_name}  -----\n')
            print(file_group.file_group_list)

    
    def list_all_downloaded_files(self):
        files_list = []

        with os.scandir(download_directory_path) as entries:
            for entry in entries:
                if re.match(self.is_file_pattern, entry.name):
                    file_name = entry.name

                files_list.append(file_name)

        return files_list
    




class FileGroup:

    def __init__(self, folder_group_name, file_format_patterns_list):
        self.folder_group_name = folder_group_name
        self.file_format_patterns_list = file_format_patterns_list
        self.file_group_list = []

    def filter_file(self, file_name):
        for file_format_pattern in self.file_format_patterns_list:
            if re.match(file_format_pattern, file_name):
                self.file_group_list.append(file_name)



class PdfGroup(FileGroup):

    def __init__(self):

        pdf_pattern = create_file_format_pattern('pdf')

        patterns_list = [
            pdf_pattern
        ]

        super().__init__('PDFs', patterns_list)



class ImageGroup(FileGroup):

    def __init__(self):

        jpeg_pattern = create_file_format_pattern('jpeg')
        jpg_pattern = create_file_format_pattern('jpg')
        png_pattern = create_file_format_pattern('png')
        svg_pattern = create_file_format_pattern('svg')

        patterns_list = [
            jpeg_pattern,
            jpg_pattern,
            png_pattern,
            svg_pattern
        ]

        super().__init__('Images', patterns_list)



class ExecutableGroup(FileGroup):

    def __init__(self):

        exe_pattern = create_file_format_pattern('exe')

        patterns_list = [
            exe_pattern
        ]

        super().__init__('Executables', patterns_list)



Setup()