from rest_framework import serializers
from banners.models import Banners


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ['id', 'title', 'description', 'link', 'image']
