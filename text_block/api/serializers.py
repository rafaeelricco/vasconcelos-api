from rest_framework import serializers
from text_block.models import TextBlock


class TextBlockSerializer(serializers.ModelSerializer):
    image_file = serializers.SerializerMethodField()

    class Meta:
        model = TextBlock
        fields = ["text", "image_file"]

    def get_image_file(self, obj):
        if obj.image_file:
            request = self.context.get("request")
            return request.build_absolute_uri(obj.image_file.url)
        return None
