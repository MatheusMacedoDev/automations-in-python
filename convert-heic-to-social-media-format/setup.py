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

            image = Image.open(f'{self.original_folder_path}/{original_image_name}')

            print('Imagem Original:')
            self.log_image_data(image)

            resized_image = self.resize_image(image)

            converted_image = image.convert('RGB')

            converted_image_new_path = f'{self.converted_folder_path}/{original_image_name}.{self.final_image_format}'

            converted_image.save(
                fp = converted_image_new_path,
                optimize = True,
                quality = self.final_image_quality
            )

            converted_image = Image.open(converted_image_new_path)

            print('Imagem Convertida:')
            self.log_image_data(converted_image)


    def resize_image(self, image):

        new_width = int(image.width * self.final_image_size_percentage)
        new_height = int(image.height * self.final_image_size_percentage)
        new_size = (new_width, new_height)

        resized_image = image.resize(new_size)


    def log_image_data(self, image):

        print('\n' + '-=' * 20)

        print(f'{image.filename}')
        print(f'Formato do arquivo: {image.format.upper()}')
        print(f'Tamanho da imagem: {image.size}')
        print(f'Tamanho do arquivo: {str(len(image.fp.read())/1000)}Kb')

        print()




setup = ConverterSetup(
    final_image_format='png',
    final_image_quality=40,
    final_image_size_percentage=0.35,
    original_folder_path='./original-images',
    converted_folder_path='./converted-images'
)

setup.run()