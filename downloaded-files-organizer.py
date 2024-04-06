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

        all_files = self.list_all_downloaded_files()

        pdfPattern = self.create_file_format_pattern('pdf')
        jpegPattern = self.create_file_format_pattern('jpeg')
        jpgPattern = self.create_file_format_pattern('jpg')
        pngPattern = self.create_file_format_pattern('png')
        svgPattern = self.create_file_format_pattern('svg')
        exePattern = self.create_file_format_pattern('exe')
        xlsxPattern = self.create_file_format_pattern('xlsx')
        pptxPattern = self.create_file_format_pattern('pptx')
        isoPattern = self.create_file_format_pattern('iso')
        partPattern = self.create_file_format_pattern('part')
        zipPattern = self.create_file_format_pattern('zip')
        sevenZipPattern = self.create_file_format_pattern('7z')

        image_group = []
        exe_group = []
        pdf_group = []
        spreadsheet_group = []
        os_image_group = []
        slides_group = []
        compacted_group = []
    
    def list_all_downloaded_files(self):
        files_list = []

        with os.scandir(download_directory_path) as entries:
            for entry in entries:
                if re.match(self.is_file_pattern, entry.name):
                    file_name = entry.name
                    files_list.append(file_name)

        return files_list
    
    def create_file_format_pattern(format_name):
        return fr'^[\d\w\s\.\-\+\_\(\)\[\]]+\.{format_name}$'

Setup()