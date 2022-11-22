from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from parts.models import Parts
from parts.api.serializers import PartsSerializer


class PartsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    queryset = Parts.objects.select_related(
        'family', 'subfamily').prefetch_related('model_version').all()
    serializer_class = PartsSerializer
