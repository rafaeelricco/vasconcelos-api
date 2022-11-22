from rest_framework import viewsets
from text_block.models import TextBlock
from text_block.api.serializers import TextBlockSerializer


class TextBlockViewSet(viewsets.ModelViewSet):
    queryset = TextBlock.objects.all()
    serializer_class = TextBlockSerializer
