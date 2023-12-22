from rest_framework import serializers
from images.models import Image
from rest_framework.fields import SerializerMethodField


class ImageSerializer(serializers.ModelSerializer):
    image_file = SerializerMethodField(
        method_name='get_image_file', read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'image_file']
        extra_kwargs = {
            'image_file': {'required': False, 'read_only': True}
        }

    def get_image_file(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image_file.url)
