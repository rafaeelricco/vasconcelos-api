from django.test import TestCase
from products.models import Product
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from pathlib import Path


image_path = Path("storage/media/tmp/test/A_Of.jpeg")

image = SimpleUploadedFile(
    name="test.jpg",
    content=open(image_path, "rb").read(),
    content_type="image/jpeg",
)


class ProductModelTest(TestCase):

    # test to create a product with all fields
    def test_create_product(self):
        product = Product.objects.create(
            name="Meridia 200",
            promise="Robustez e qualidade para o seu Plantio.",
            cover=image,
            launch=True,
            featured=True,
            flyer="https://www.google.com",
            youtube="https://www.youtube.com",
        )
        self.assertTrue(Product.objects.filter(id=product.id).exists())

    # test to create a product with a name that already exists
    def test_create_product_with_name_that_already_exists(self):
        Product.objects.create(
            name="Meridia 200",
            promise="Robustez e qualidade para o seu Plantio.",
            cover=image,
            launch=True,
            featured=True,
            flyer="https://www.google.com",
            youtube="https://www.youtube.com",
        )
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com",
                youtube="https://www.youtube.com",
            )

    # test to create a product with max_length of name
    def test_create_product_with_max_length_of_name(self):
        product = Product.objects.create(
            name="Meridia 200" * 100,
            promise="Robustez e qualidade para o seu Plantio.",
            cover=image,
            launch=True,
            featured=True,
            flyer="https://www.google.com",
            youtube="https://www.youtube.com",
        )
        self.assertTrue(Product.objects.filter(id=product.id).exists())

    # test to create a product with a name that contains special characters
    def test_create_product_with_name_that_contains_special_characters(self):
        with self.assertRaises(ValidationError):
            product_wrong = Product.objects.create(
                name="Meridia 200@#$%¨&*()",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com",
                youtube="https://www.youtube.com",
            )
            product_wrong.full_clean()

    # test to create a product with a promise that already exists
    def test_create_product_with_promise_that_already_exists(self):
        Product.objects.create(
            name="Meridia 200",
            promise="Robustez e qualidade para o seu Plantio.",
            cover=image,
            launch=True,
            featured=True,
            flyer="https://www.google.com",
            youtube="https://www.youtube.com",
        )
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com",
                youtube="https://www.youtube.com",
            )

    # test to create a product with max_length of promise
    def test_create_product_with_max_length_of_promise(self):
        with self.assertRaises(ValidationError):
            product_wrong = Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio." * 100,
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com",
                youtube="https://www.youtube.com",
            )
            product_wrong.full_clean()

    # test to create a product with a promise that contains special characters
    def test_create_product_with_promise_that_contains_special_characters(self):
        with self.assertRaises(ValidationError):
            product_wrong = Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.@#$%¨&*()",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com",
                youtube="https://www.youtube.com",
            )
            product_wrong.full_clean()

    # test create a flyer with a link that already exists
    def test_create_product_with_flyer_that_already_exists(self):
        Product.objects.create(
            name="Meridia 200",
            promise="Robustez e qualidade para o seu Plantio.",
            cover=image,
            launch=True,
            featured=True,
            flyer="https://www.google.com",
            youtube="https://www.youtube.com",
        )
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com",
                youtube="https://www.youtube.com",
            )

    # test create a flyer with a link that contains special characters
    def test_create_product_with_flyer_that_contains_special_characters(self):
        with self.assertRaises(ValidationError):
            product_wrong = Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com@#$%¨&*()",
                youtube="https://www.youtube.com",
            )
            product_wrong.full_clean()

    # test create a flayer with max_length of link
    def test_create_product_with_max_length_of_flyer(self):
        with self.assertRaises(ValidationError):
            product_wrong = Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com" * 1000,
                youtube="https://www.youtube.com",
            )
            product_wrong.full_clean()

    # test create a flyer with only domain
    def test_create_product_with_flyer_with_only_domain(self):
        with self.assertRaises(ValidationError):
            product_wrong = Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="google.com",
                youtube="youtube.com",
            )
            product_wrong.full_clean()

    # test create a youtube with a link that already exists
    def test_create_product_with_youtube_that_already_exists(self):
        Product.objects.create(
            name="Meridia 200",
            promise="Robustez e qualidade para o seu Plantio.",
            cover=image,
            launch=True,
            featured=True,
            flyer="https://www.google.com",
            youtube="https://www.youtube.com",
        )
        # try to create a product with the same youtube
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com",
                youtube="https://www.youtube.com",
            )

    # test create a youtube with max_length of link
    def test_create_product_with_max_length_of_youtube(self):
        with self.assertRaises(ValidationError):
            product_wrong = Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com",
                youtube="https://www.youtube.com" * 1000,
            )
            product_wrong.full_clean()

    # test create a youtube with a link that contains special characters
    def test_create_product_with_youtube_that_contains_special_characters(self):
        with self.assertRaises(ValidationError):
            product_wrong = Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com",
                youtube="https://www.youtube.com@#$%¨&*()",
            )
            product_wrong.full_clean()

    # test create a youtube with only domain
    def test_create_product_with_youtube_with_only_domain(self):
        with self.assertRaises(ValidationError):
            product_wrong = Product.objects.create(
                name="Meridia 200",
                promise="Robustez e qualidade para o seu Plantio.",
                cover=image,
                launch=True,
                featured=True,
                flyer="https://www.google.com",
                youtube="youtube.com",
            )
            product_wrong.full_clean()
