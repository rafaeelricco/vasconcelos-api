from pathlib import Path
from django.test import TestCase
from banners.models import Banners
from essential_generators import DocumentGenerator
from django.core.files.uploadedfile import SimpleUploadedFile

gen = DocumentGenerator()

image_path = Path("storage/media/tmp/test/A_Of.jpeg")

image = SimpleUploadedFile(
    name="test.jpg",
    content=open(image_path, "rb").read(),
    content_type="image/jpeg",
)


class TestBannerModel(TestCase):

    # test to create a new banner
    def test_create_banner(self):
        banner = Banners.objects.create(
            title=gen.sentence(),
            description=gen.paragraph(),
            link=gen.url(),
            image=image,
        )
        self.assertEqual(banner.title, banner.title)
        self.assertEqual(banner.description, banner.description)
        self.assertEqual(banner.link, banner.link)
        self.assertEqual(banner.image, banner.image)

    # test to create a invalid banner
    def test_create_invalid_banner(self):
        with self.assertRaises(Exception) as context:
            banner = Banners.objects.create(
                title=gen.paragraph(nb_sentences=10),
                description=gen.paragraph(),
                link=gen.url(),
                image=image,
            )

    # test to create a banner with invalid link and wrong image
    def test_create_invalid_banner(self):
        with self.assertRaises(Exception):
            banner = Banners.objects.create(
                title=gen.sentence(),
                description=gen.paragraph(),
                link="test@gmail.com",
                image="image.webp",
            )

        with self.assertRaises(Exception):
            banner = Banners.objects.create(
                title=gen.sentence(),
                description=gen.paragraph(),
                link=gen.phone(),
                image=10192,
            )

        with self.assertRaises(Exception):
            banner = Banners.objects.create(
                title=gen.sentence(),
                description=gen.paragraph(),
                link=gen.floating(),
                image="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
            )
