from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    im_conv = im.convert('RGB')
    im_io = BytesIO()
    im_conv.save(im_io, 'JPEG', quality=80)
    new_image = File(im_io, name=image.name)
    return new_image
