from PIL import Image
from pillow_heif import register_heif_opener
from re import match
from os import scandir

register_heif_opener()

class ConverterSetup:

    def __init__(self, final_image_format, final_image_size_percentage, final_image_quality,
                 original_folder_path, converted_folder_path):

        self.is_heic_image_pattern = r'^[\d\w\s\.\-\+\_\(\)\[\]]+\.(heic|HEIC)$'

        self.final_image_format = final_image_format
        self.final_image_size_percentage = final_image_size_percentage
        self.final_image_quality = final_image_quality

        self.original_folder_path = original_folder_path
        self.converted_folder_path = converted_folder_path


    def run(self):
        original_images = self.list_original_images()

        print('Original Images')
        print(original_images)

        self.transform_images(original_images)


    def list_original_images(self):
        original_list = []

        with scandir(self.original_folder_path) as entries:
            for entry in entries:
                if match(self.is_heic_image_pattern, entry.name):
                    heic_image = entry.name
                    original_list.append(heic_image)

        return original_list



    def transform_images(self, original_images):
        for original_image_name in original_images:
            image = Image.open(f'{self.original_folder_path}{original_image_name}')

            converted_image = image.convert('RGB')

            converted_image.save(
                fp = f'{self.converted_folder_path}/{original_image_name}.{final_image_format}',
                optimize = True,
                quality = self.final_image_quality
            )





setup = ConverterSetup(
    final_image_format='png',
    final_image_quality=40,
    final_image_size_percentage=0.35,
    original_folder_path='./original-images',
    converted_folder_path='./converted-images'
)

setup.run()