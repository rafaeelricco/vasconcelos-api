from rest_framework import viewsets
from categories.models import (
    Category,
    Cultures,
    Disponibility,
    Family,
    Launch,
    ModelsAndVersions,
    SizeOfArea,
    SubFamily,
)
from categories.api.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CulturesViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]
    queryset = Cultures.objects.all()
    serializer_class = CategorySerializer


class DisponibilityViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]
    queryset = Disponibility.objects.all()
    serializer_class = CategorySerializer


class FamilyViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]
    queryset = Family.objects.all()
    serializer_class = CategorySerializer


class LaunchViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]
    queryset = Launch.objects.all()
    serializer_class = CategorySerializer


class ModelsAndVersionsViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]
    queryset = ModelsAndVersions.objects.all()
    serializer_class = CategorySerializer


class SizeOfAreaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]
    queryset = SizeOfArea.objects.all()
    serializer_class = CategorySerializer


class SubFamilyViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]
    queryset = SubFamily.objects.all()
    serializer_class = CategorySerializer
