from rest_framework import viewsets
from parts.images.models import Image
from parts.images.api.serializers import ImageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    queryset = Image.objects.select_related('parts').all()
    serializer_class = ImageSerializer
