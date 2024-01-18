from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from retail_chain.models import RetailChain
from retail_chain.permissions import IsActivePermissions
from retail_chain.serializers import RetailChainSerializer

# Create your views here.


class RetailChainViewSet(ModelViewSet):
    """CRUD для модели RetailChain"""

    serializer_class = RetailChainSerializer
    queryset = RetailChain.objects.all()
    permission_classes = [IsActivePermissions]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("contacts__country",)
