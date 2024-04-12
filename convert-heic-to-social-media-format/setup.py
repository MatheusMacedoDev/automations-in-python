from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

class ConverterSetup:
    def __init__(self, final_image_format, final_image_size_percentage, final_image_quality):
        self.final_image_format = final_image_format
        self.final_image_size_percentage = final_image_size_percentage
        self.final_image_quality = final_image_quality

ConverterSetup(
    final_image_format='png',
    final_image_quality=40,
    final_image_size_percentage=0.35
)