from rest_framework import serializers
from categories.models import (
    Category,
    Family,
    SubFamily,
    ModelsAndVersions,
    Cultures,
    SizeOfArea,
    Disponibility,
    Launch,
)


class DisponibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibility
        fields = ["name", "slug"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]


class CulturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultures
        fields = ["name", "slug"]


class SizeOfAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeOfArea
        fields = ["name", "slug"]


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ["id", "name", "slug"]


class SubFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubFamily
        fields = ["name", "slug"]


class ModelsAndVersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelsAndVersions
        fields = ["name", "slug"]


class LaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launch
        fields = ["name", "slug"]
