from rest_framework import viewsets
from banners.models import Banners
from banners.api.serializers import BannersSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


class BannersViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    queryset = Banners.objects.all()
    serializer_class = BannersSerializer
