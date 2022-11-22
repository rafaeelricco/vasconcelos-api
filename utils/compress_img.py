from io import BytesIO
from PIL import Image
from django.core.files import File
from essential_generators import DocumentGenerator

gen = DocumentGenerator()


def compress(image):
    im = Image.open(image)
    im_conv = im.convert("RGB")
    im_io = BytesIO()
    im_conv.save(im_io, "JPEG", quality=40)
    gen_file_name = r"{}.jpeg".format(gen.name())
    new_image = File(im_io, name=gen_file_name)
    return new_image
