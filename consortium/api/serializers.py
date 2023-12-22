from rest_framework import serializers
from consortium.models import Consortium


class ConsortiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consortium
        fields = ['id', 'full_name', 'email', 'phone', 'state',
                  'city', 'accept_contact', 'product_request']
