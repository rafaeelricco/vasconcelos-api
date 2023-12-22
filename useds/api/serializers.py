from rest_framework import serializers
from useds.models import Useds
from useds.images.api.serializers import ImageSerializer


class UsedSerializers(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Useds
        fields = ['id', 'name', 'branding', 'description',
                  'cover', 'images', 'model', 'year', 'price', 'slug']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['slug'].disabled = True
