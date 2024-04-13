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

        self.convert_images(original_images)

        converted_images = self.list_converted_images()

        self.compress_image(converted_images)


    def list_original_images(self):

        original_list = []

        with scandir(self.original_folder_path) as entries:
            for entry in entries:
                if match(self.is_heic_image_pattern, entry.name):
                    heic_image = entry.name
                    original_list.append(heic_image)

        return original_list

    
    def list_converted_images(self):

        converted_list = []

        with scandir(self.converted_folder_path) as entries:
            for entry in entries:
                if not match('.gitkeep', entry.name):
                    converted_list.append(entry.name)

        return converted_list


    def convert_images(self, original_images):

        for original_image_name in original_images:

            image = Image.open(f'{self.original_folder_path}/{original_image_name}')

            converted_image = image.convert('RGB')

            image_format_name = image.format
            if (image.format.upper() == 'HEIF'):
                image_format_name = 'HEIC'

            converted_image_new_path = f'{self.converted_folder_path}/{original_image_name.replace(f'.{image_format_name}', '').replace(f'.{image_format_name.upper()}', '')}.{self.final_image_format}'

            converted_image.save(
                fp = converted_image_new_path,
            )

            converted_image = Image.open(converted_image_new_path)


    def compress_image(self, converted_images):

        for converted_image_name in converted_images:

            converted_image = Image.open(f'{self.converted_folder_path}/{converted_image_name}')

            resized_image = self.resize_image(converted_image)

            converted_image_new_path = f'{self.converted_folder_path}/{converted_image_name}'

            resized_image.save(
                fp = converted_image_new_path,
                optimize = True,
                quality = self.final_image_quality
            )


    def resize_image(self, image):

        new_width = int(image.width * self.final_image_size_percentage)
        new_height = int(image.height * self.final_image_size_percentage)
        new_size = (new_width, new_height)

        resized_image = image.resize(new_size)

        return resized_image


    def log_image_data(self, image):

        print('\n' + '-=' * 20)

        print(f'{image.filename}')
        print(f'Formato do arquivo: {image.format.upper()}')
        print(f'Tamanho da imagem: {image.size}')
        print(f'Tamanho do arquivo: {str(len(image.fp.read())/1000)}Kb')

        print()




setup = ConverterSetup(
    final_image_format='png',
    final_image_quality=36,
    final_image_size_percentage=0.28,
    original_folder_path='./original-images',
    converted_folder_path='./converted-images'
)

setup.run()