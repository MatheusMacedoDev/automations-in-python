# Idea
# - List all files and organize by file format
# - Move organized files to your respective folder

class Setup:
    def __init__(self):
        download_directory_path = 'C:/Users/mathe/Downloads'
        is_file_pattern = r'^[\d\w\s\.\-\+\_\(\)\[\]]+\.[0-9a-z]{2,5}$'

        image_group = []
        exe_group = []
        pdf_group = []
        spreadsheet_group = []
        os_image_group = []