from rest_framework import viewsets
from images.api.serializers import ImageSerializer
from images.models import Image
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    queryset = Image.objects.select_related('product').all()
    serializer_class = ImageSerializer
