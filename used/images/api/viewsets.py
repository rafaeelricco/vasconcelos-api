from rest_framework import viewsets
from used.images.models import Image
from used.images.api.serializers import ImageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
