from django.test import TestCase
from categories.models import (
    Category,
    Cultures,
    Disponibility,
    Family,
    SizeOfArea,
    SubFamily,
    ModelsAndVersions,
    Launch,
)
from essential_generators import DocumentGenerator

gen = DocumentGenerator()


class TestCategoryModel(TestCase):
    # test if the model is created
    def test_create_category(self):
        # test create category
        self.category = Category.objects.create(name=gen.name())
        self.assertTrue(len(self.category.name) <= 30)

        isinstance(self.category, Category)
        isinstance(self.category.name, str)
        isinstance(self.category.id, int)

    # test create invalid category
    def test_create_invalid_category(self):
        with self.assertRaises(Exception):
            self.category = Category.objects.create(name=gen.paragraph(nb_sentences=10))


class TestCulturesModel(TestCase):
    # test if the model is created
    def test_create_cultures(self):
        # test create cultures
        self.cultures = Cultures.objects.create(name=gen.name())
        self.assertTrue(len(self.cultures.name) <= 30)

        isinstance(self.cultures, Cultures)
        isinstance(self.cultures.name, str)
        isinstance(self.cultures.id, int)

    # test create invalid cultures
    def test_create_invalid_cultures(self):
        with self.assertRaises(Exception):
            self.cultures = Cultures.objects.create(name=gen.paragraph(nb_sentences=10))


class TestDisponibilityModel(TestCase):
    # test if the model is created
    def test_create_disponibility(self):
        # test create disponibility
        self.disponibility = Disponibility.objects.create(name=gen.name())
        self.assertTrue(len(self.disponibility.name) <= 30)

        isinstance(self.disponibility, Disponibility)
        isinstance(self.disponibility.name, str)
        isinstance(self.disponibility.id, int)

    # test create invalid disponibility
    def test_create_invalid_disponibility(self):
        with self.assertRaises(Exception):
            self.disponibility = Disponibility.objects.create(
                name=gen.paragraph(nb_sentences=10)
            )


class TestFamilyModel(TestCase):
    # test if the model is created
    def test_create_family(self):
        # test create family
        self.family = Family.objects.create(name=gen.name())
        self.assertTrue(len(self.family.name) <= 30)

        isinstance(self.family, Family)
        isinstance(self.family.name, str)
        isinstance(self.family.id, int)

    # test create invalid family
    def test_create_invalid_family(self):
        with self.assertRaises(Exception):
            self.family = Family.objects.create(name=gen.paragraph(nb_sentences=10))


class TestSizeOfAreaModel(TestCase):
    # test if the model is created
    def test_create_size_of_area(self):
        # test create size_of_area
        self.size_of_area = SizeOfArea.objects.create(name=gen.name())
        self.assertTrue(len(self.size_of_area.name) <= 30)

        isinstance(self.size_of_area, SizeOfArea)
        isinstance(self.size_of_area.name, str)
        isinstance(self.size_of_area.id, int)

    # test create invalid size_of_area
    def test_create_invalid_size_of_area(self):
        with self.assertRaises(Exception):
            self.size_of_area = SizeOfArea.objects.create(
                name=gen.paragraph(nb_sentences=10)
            )


class TestSubFamilyModel(TestCase):
    # test if the model is created
    def test_create_sub_family(self):
        # test create sub_family
        self.sub_family = SubFamily.objects.create(name=gen.name())
        self.assertTrue(len(self.sub_family.name) <= 30)

        isinstance(self.sub_family, SubFamily)
        isinstance(self.sub_family.name, str)
        isinstance(self.sub_family.id, int)

    # test create invalid sub_family
    def test_create_invalid_sub_family(self):
        with self.assertRaises(Exception):
            # test create invalid sub_family expect exception
            self.sub_family = SubFamily.objects.create(
                name=gen.paragraph(nb_sentences=10)
            )


class TestModelsAndVersionsModel(TestCase):
    # test if the model is created
    def test_create_models_and_versions(self):
        # test create models_and_versions
        self.models_and_versions = ModelsAndVersions.objects.create(name=gen.name())
        self.assertTrue(len(self.models_and_versions.name) <= 30)

        isinstance(self.models_and_versions, ModelsAndVersions)
        isinstance(self.models_and_versions.name, str)
        isinstance(self.models_and_versions.id, int)

    # test create invalid models_and_versions
    def test_create_invalid_models_and_versions(self):
        with self.assertRaises(Exception):
            self.models_and_versions = ModelsAndVersions.objects.create(
                name=gen.paragraph(nb_sentences=10)
            )


class TestLaunchModel(TestCase):
    # test if the model is created
    def test_create_launch(self):
        # test create launch
        self.launch = Launch.objects.create(name=gen.name())
        self.assertTrue(len(self.launch.name) <= 30)

        isinstance(self.launch, Launch)
        isinstance(self.launch.name, str)
        isinstance(self.launch.id, int)

    # test create invalid launch
    def test_create_invalid_launch(self):
        with self.assertRaises(Exception):
            self.launch = Launch.objects.create(name=gen.paragraph(nb_sentences=10))
