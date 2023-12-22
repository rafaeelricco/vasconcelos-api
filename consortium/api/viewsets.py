from rest_framework import viewsets
from consortium.models import Consortium
from consortium.api.serializers import ConsortiumSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ConsortiumViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Consortium.objects.all()
    serializer_class = ConsortiumSerializer
