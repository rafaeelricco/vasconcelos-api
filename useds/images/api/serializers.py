
from rest_framework import serializers
from useds.images.models import Image
from rest_framework.fields import SerializerMethodField


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_file')

    class Meta:
        model = Image
        fields = ['id', 'image_url']
        extra_kwargs = {
            'image_url': {'required': False, 'read_only': True}
        }

    def get_image_file(self, obj):
        request = self.context.get('request')
        image_url = obj.image_url.url
        return request.build_absolute_uri(image_url)
