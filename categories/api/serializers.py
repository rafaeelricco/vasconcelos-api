from rest_framework import serializers
from categories.models import Category, Family, SubFamily, ModelsAndVersions, Cultures, SizeOfArea, Disponibility, Launch


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class CulturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultures
        fields = ['id', 'name', 'slug']


class SizeOfAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeOfArea
        fields = ['id', 'name', 'slug']


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['id', 'name', 'slug']


class SubFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubFamily
        fields = ['id', 'name', 'slug']


class ModelsAndVersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelsAndVersions
        fields = ['id', 'name', 'slug']


class DisponibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibility
        fields = ['id', 'name', 'slug']


class LaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launch
        fields = ['id', 'name', 'slug']
