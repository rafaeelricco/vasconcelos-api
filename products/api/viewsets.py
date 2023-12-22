from rest_framework import viewsets
from products.models import Product
from products.api.serializers import ProductSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from products.models import Featured
from products.api.serializers import FeaturedSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    queryset = Product.objects.select_related(
        'category').prefetch_related('area', 'cultures').all()
    serializer_class = ProductSerializers


class FeaturedViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    queryset = Featured.objects.all()
    serializer_class = FeaturedSerializer
