from rest_framework import serializers
from parts.images.api.serializers import ImageSerializer
from categories.api.serializers import FamilySerializer, SubFamilySerializer, ModelsAndVersionsSerializer
from parts.models import Parts


class PartsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    family = FamilySerializer(many=False,)
    subfamily = SubFamilySerializer(many=False)
    model_version = ModelsAndVersionsSerializer(many=True)

    class Meta:
        model = Parts
        fields = ['id', 'name', 'code', 'branding', 'slug',
                  'description', 'images',
                  'family', 'subfamily', 'model_version', ]
