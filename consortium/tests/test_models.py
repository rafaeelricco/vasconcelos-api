from django.test import TestCase
from consortium.models import Consortium
from essential_generators import DocumentGenerator
from django.core.exceptions import ValidationError

gen = DocumentGenerator()


class TestConsortiumModel(TestCase):

    # test creating a consortium with invalid email
    def test_create_consortium_invalid_email(self):
        with self.assertRaises(ValidationError):
            consortium = Consortium.objects.create(
                full_name=gen.name(),
                email=gen.domain(),
                phone=gen.phone(),
                state=gen.domain(),
                city=gen.domain(),
                product_request=gen.word(),
                accept_contact=True,
            )
            consortium.full_clean()

    # test creating a consortium with invalid phone
    def test_create_consortium_invalid_phone(self):
        with self.assertRaises(ValidationError):
            consortium = Consortium.objects.create(
                full_name=gen.name(),
                email=gen.email(),
                phone=gen.domain(),
                state=gen.domain(),
                city=gen.domain(),
                product_request=gen.word(),
                accept_contact=True,
            )
            consortium.full_clean()

    # test creating a consortium with invalid state
    def test_create_consortium_invalid_state(self):
        with self.assertRaises(ValidationError):
            consortium = Consortium.objects.create(
                full_name=gen.name(),
                email=gen.email(),
                phone=gen.phone(),
                state=gen.domain(),
                city=gen.domain(),
                product_request=gen.word(),
                accept_contact=True,
            )
            consortium.full_clean()

    # test creating a consortium with invalid city
    def test_create_consortium_invalid_city(self):
        with self.assertRaises(ValidationError):
            consortium = Consortium.objects.create(
                full_name=gen.name(),
                email=gen.email(),
                phone=gen.phone(),
                state=gen.domain(),
                city=gen.domain(),
                product_request=gen.word(),
                accept_contact=True,
            )
            consortium.full_clean()
