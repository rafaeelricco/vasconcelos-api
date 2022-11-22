from rest_framework import serializers
from products.models import Product
from products.images.api.serializers import ImageSerializer
from categories.api.serializers import CategorySerializer
from categories.api.serializers import CulturesSerializer
from categories.api.serializers import SizeOfAreaSerializer
from categories.api.serializers import DisponibilitySerializer
from text_block.api.serializers import TextBlockSerializer
from products.images.api.serializers import ImageSerializer


class ProductSerializers(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    category = CategorySerializer(many=False, read_only=True)
    disponibility = DisponibilitySerializer(many=False, read_only=True)
    cultures = CulturesSerializer(many=True, read_only=True)
    area = SizeOfAreaSerializer(many=True, read_only=True)
    text_blocks = TextBlockSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "promise",
            "cover",
            "flyer",
            "youtube",
            "launch",
            "featured",
            "text_blocks",
            "images",
            "category",
            "area",
            "cultures",
            "disponibility",
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["slug"].disabled = True
