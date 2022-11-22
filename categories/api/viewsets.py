from rest_framework import viewsets
from categories.models import Category
from categories.api.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
