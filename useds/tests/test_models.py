from django.test import TestCase
from useds.models import Useds


class TestUsedsModel(TestCase):

    # test to create one used
    def test_create_used(self):
        used_data = {
            "name": "Carro",
            "branding": "Fiat",
            "description": "Carro usado",
            "cover": "",
            "model": "Uno",
            "year": "2020",
            "price": "R$ 10.000,00",
        }
        useds = Useds.objects.create(**used_data)

        self.assertEqual(useds.name, used_data["name"])
        self.assertEqual(useds.branding, used_data["branding"])
        self.assertEqual(useds.description, used_data["description"])
        self.assertEqual(useds.cover, used_data["cover"])
        self.assertEqual(useds.model, used_data["model"])
        self.assertEqual(useds.year, used_data["year"])
        self.assertEqual(useds.price, used_data["price"])

    # try create a used with invalid name, is expected error
    def test_create_used_with_invalid_name(self):
        with self.assertRaises(Exception, msg="Nome do produto inválido"):
            used_invalid_name = Useds.objects.create(
                name="Carro@",
                branding="Fiat",
                description="Carro usado",
                cover="",
                model="Uno",
                year="2020",
                price="R$ 10.000,00",
            )
            used_invalid_name.full_clean()

    # teste to create a used with empty name, is expected error
    def test_create_used_with_empty_name(self):
        with self.assertRaises(Exception, msg="Nome do produto não pode ser vazio"):
            used_empty_name = Useds.objects.create(
                name=" ",
                branding="Fiat",
                description="Carro usado",
                cover="",
                model="Uno",
                year="2020",
                price="R$ 10.000,00",
            )
            used_empty_name.full_clean()

    # test to create a used with invalid branding, is expected error
    def test_create_used_with_invalid_branding(self):
        with self.assertRaises(Exception, msg="Marca do produto inválida"):
            used_invalid_branding = Useds.objects.create(
                name="Carro",
                branding="Fiat@",
                description="Carro usado",
                cover="",
                model="Uno",
                year="2020",
                price="R$ 10.000,00",
            )
            used_invalid_branding.full_clean()

    # test to create a used with empty branding, is expected error
    def test_create_used_with_empty_branding(self):
        with self.assertRaises(Exception, msg="Marca do produto não pode ser vazia"):
            used_empty_branding = Useds.objects.create(
                name="Carro",
                branding=" ",
                description="Carro usado",
                cover="",
                model="Uno",
                year="2020",
                price="R$ 10.000,00",
            )
            used_empty_branding.full_clean()

    # test to create a used with invalid model, is expected error
    def test_create_used_with_invalid_model(self):
        with self.assertRaises(Exception, msg="Modelo do produto é inválido"):
            used_invalid_model = Useds.objects.create(
                name="Carro",
                branding="Fiat",
                description="Carro usado",
                cover="",
                model="Uno@",
                year="2020",
                price="R$ 10.000,00",
            )
            used_invalid_model.full_clean()

    # test to create a used with empty model, is expected error
    def test_create_used_with_empty_model(self):
        with self.assertRaises(Exception, msg="Modelo do produto não pode ser vazio"):
            used_empty_model = Useds.objects.create(
                name="Carro",
                branding="Fiat",
                description="Carro usado",
                cover="",
                model=" ",
                year="2020",
                price="R$ 10.000,00",
            )
            used_empty_model.full_clean()

    # test to create a used with invalid year, is expected error
    def test_create_used_with_invalid_year(self):
        with self.assertRaises(Exception, msg="Ano do produto é inválido"):
            used_invalid_year = Useds.objects.create(
                name="Carro",
                branding="Fiat",
                description="Carro usado",
                cover="",
                model="Uno",
                year="2020@",
                price="R$ 10.000,00",
            )
            used_invalid_year.full_clean()

    # test to create a used with empty year, is expected error
    def test_create_used_with_empty_year(self):
        with self.assertRaises(Exception, msg="Ano do produto não pode ser vazio"):
            used_empty_year = Useds.objects.create(
                name="Carro",
                branding="Fiat",
                description="Carro usado",
                cover="",
                model="Uno",
                year=" ",
                price="R$ 10.000,00",
            )
            used_empty_year.full_clean()

    # test to create a used with invalid price, is expected error
    def test_create_used_with_invalid_price(self):
        with self.assertRaises(Exception, msg="Preço do produto é inválido"):
            used_invalid_price = Useds.objects.create(
                name="Carro",
                branding="Fiat",
                description="Carro usado",
                cover="",
                model="Uno",
                year="2020",
                price="R$ 10.000,00@",
            )
            used_invalid_price.full_clean()

    # test to create a used with empty price, is expected error
    def test_create_used_with_empty_price(self):
        with self.assertRaises(Exception, msg="Preço do produto não pode ser vazio"):
            used_empty_price = Useds.objects.create(
                name="Carro",
                branding="Fiat",
                description="Carro usado",
                cover="",
                model="Uno",
                year="2020",
                price=" ",
            )
            used_empty_price.full_clean()
