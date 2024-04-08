import os
import re
import shutil
from pathlib import Path

# Idea
# - List all files
# - Organize by file format
# - Move organized files to your respective folder

download_directory_path = 'C:/Users/mathe/Downloads'

def create_file_format_pattern(format_name):
    return fr'^[\d\w\s\.\-\+\_\(\)\[\]]+\.({format_name}|{format_name.upper()})$'

class Setup:

    def __init__(self):

        self.is_file_pattern = r'^[\d\w\s\.\-\+\_\(\)\[\]]+\.[0-9A-Za-z]{2,5}$'

        self.all_files = self.list_all_downloaded_files()
        self.remaining_files = self.all_files.copy()

        self.file_groups = [
            PdfGroup(),
            ImageGroup(),
            ExecutableGroup(),
            OfficeGroup(),
            OSImageGroup(),
            CompactedGroup()
        ]

        for file in self.all_files:

            for file_group in self.file_groups:
                is_matching = file_group.filter_file(file)

                if is_matching:
                    self.remaining_files.remove(file)
                    break

                
        for file_group in self.file_groups:
            print(f'\n-----  {file_group.folder_group_name}  -----\n')
            print(file_group.group_file_list)

        print(f'\n-----  Remaining files  -----\n')
        print(self.remaining_files)
        print()

        for file_group in self.file_groups:
            file_group.create_directory_if_not_exist()
            file_group.move_to_correct_directory()

    
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
        self.folder_path_text = f'{download_directory_path}/{self.folder_group_name}'
        self.file_format_patterns_list = file_format_patterns_list
        self.group_file_list = []

    def filter_file(self, file_name):

        for file_format_pattern in self.file_format_patterns_list:

            if re.match(file_format_pattern, file_name):
                self.group_file_list.append(file_name)
                return True

        return False

    def create_directory_if_not_exist(self):
        directory_path = Path(self.folder_path_text)
        directory_path.mkdir(exist_ok=True)

    def move_to_correct_directory(self):

        for file in self.group_file_list:
            file_path = f'{download_directory_path}/{file}'
            shutil.move(file_path, self.folder_path_text)



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
        heic_pattern = create_file_format_pattern('heic')

        patterns_list = [
            jpeg_pattern,
            jpg_pattern,
            png_pattern,
            svg_pattern,
            heic_pattern
        ]

        super().__init__('Images', patterns_list)



class ExecutableGroup(FileGroup):

    def __init__(self):

        exe_pattern = create_file_format_pattern('exe')

        patterns_list = [
            exe_pattern
        ]

        super().__init__('Executables', patterns_list)



class OfficeGroup(FileGroup):

    def __init__(self):

        xlsx_pattern = create_file_format_pattern('xlsx')
        pptx_pattern = create_file_format_pattern('pptx')

        patterns_list = [
            xlsx_pattern,
            pptx_pattern
        ]

        super().__init__('Office', patterns_list)



class OSImageGroup(FileGroup):

    def __init__(self):

        iso_pattern = create_file_format_pattern('iso')
        part_pattern = create_file_format_pattern('part')

        patterns_list = [
            iso_pattern,
            part_pattern
        ]

        super().__init__('OSImages', patterns_list)



class CompactedGroup(FileGroup):

    def __init__(self):

        zip_pattern = create_file_format_pattern('zip')
        seven_zip_pattern = create_file_format_pattern('7z')

        patterns_list = [
            zip_pattern,
            seven_zip_pattern
        ]

        super().__init__('Compacted', patterns_list)



Setup()