from rest_framework import serializers
from products.models import Product
from images.api.serializers import ImageSerializer
from categories.api.serializers import CategorySerializer
from categories.api.serializers import CulturesSerializer
from categories.api.serializers import SizeOfAreaSerializer
from products.models import Featured


class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fields = ['id', 'name', 'description', 'link', 'image']


class ProductSerializers(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    category = CategorySerializer(many=False, read_only=True)
    cultures = CulturesSerializer(many=True, read_only=True)
    area = SizeOfAreaSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'promise',
                  'description', 'cover', 'flyer', 'youtube', 'category', 'area', 'cultures','launch', 'disponibility', 'images']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['slug'].disabled = True
