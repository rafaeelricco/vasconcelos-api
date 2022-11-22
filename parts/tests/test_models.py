from django.test import TestCase
from parts.models import Parts
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from essential_generators import DocumentGenerator
from django.db.utils import IntegrityError
from pathlib import Path

gen = DocumentGenerator()

image_path = Path("storage/media/tmp/test/A_Of.jpeg")

image = SimpleUploadedFile(
    name="test.jpg",
    content=open(image_path, "rb").read(),
    content_type="image/jpeg",
)


class PartsModelTest(TestCase):
    # test to create a one part with all fields filled
    def test_create_one_part(self):
        part = Parts.objects.create(
            name="Teste",
            code="Teste",
            branding="Teste",
            description="Teste",
        )
        self.assertEqual(part.name, "Teste")
        self.assertEqual(part.code, "Teste")
        self.assertEqual(part.branding, "Teste")
        self.assertEqual(part.description, "Teste")

    # test to create a name with invalid characters
    def test_create_one_part_with_invalid_name(self):
        with self.assertRaises(ValidationError):
            part = Parts.objects.create(
                name=gen.email(),
            )
            part.full_clean()

    # test to create a name with more than 50 characters
    def test_create_one_part_with_name_more_than_50_characters(self):
        with self.assertRaises(ValidationError):
            part = Parts.objects.create(
                name=gen.sentence(),
            )
            part.full_clean()

    # test to create a name with less than 5 characters
    def test_create_one_part_with_name_less_than_5_characters(self):
        with self.assertRaises(ValidationError):
            part = Parts.objects.create(
                name="T",
            )
            part.full_clean()

    # test to create a code with invalid characters
    def test_create_one_part_with_invalid_code(self):
        with self.assertRaises(ValidationError):
            part = Parts.objects.create(
                code=gen.email(),
            )
            part.full_clean()

    # test to create a branding with invalid characters
    def test_create_one_part_with_invalid_branding(self):
        with self.assertRaises(ValidationError):
            part = Parts.objects.create(
                branding=gen.email(),
            )
            part.full_clean()

    # test to create a branding with more than 50 characters
    def test_create_one_part_with_branding_more_than_50_characters(self):
        with self.assertRaises(ValidationError):
            part = Parts.objects.create(
                branding=gen.paragraph(max_sentences=100),
            )
            part.full_clean()

    # test to create a branding with less than 5 characters
    def test_create_one_part_with_branding_less_than_5_characters(self):
        with self.assertRaises(ValidationError):
            part = Parts.objects.create(
                branding="T",
            )
            part.full_clean()

    # test to create a part with a name that already exists
    def test_create_one_part_with_name_that_already_exists(self):
        with self.assertRaises(IntegrityError):
            part = Parts.objects.create(
                name="Teste",
            )
            part = Parts.objects.create(
                name="Teste",
            )
            part.full_clean()

    # test to create a part with a code that already exists
    def test_create_one_part_with_code_that_already_exists(self):
        with self.assertRaises(IntegrityError):
            part = Parts.objects.create(
                code="Teste",
            )
            part = Parts.objects.create(
                code="Teste",
            )
            part.full_clean()

    # test to create a part with a branding that already exists
    def test_create_one_part_with_branding_that_already_exists(self):
        with self.assertRaises(IntegrityError):
            part = Parts.objects.create(
                branding="Teste",
            )
            part = Parts.objects.create(
                branding="Teste",
            )
            part.full_clean()

    # test to create a part with a description that already exists
    def test_create_one_part_with_description_that_already_exists(self):
        with self.assertRaises(IntegrityError):
            part = Parts.objects.create(
                description="Teste",
            )
            part = Parts.objects.create(
                description="Teste",
            )
            part.full_clean()

    # test to create a part with a image that already exists
    def test_create_one_part_with_image_that_already_exists(self):
        with self.assertRaises(IntegrityError):
            part = Parts.objects.create(
                cover=image,
            )
            part = Parts.objects.create(
                cover=image,
            )
            part.full_clean()
