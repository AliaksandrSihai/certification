from rest_framework.routers import DefaultRouter

from retail_chain.apps import RetailChainConfig
from retail_chain.views import RetailChainViewSet

routers = DefaultRouter()
routers.register(r"retailchain", RetailChainViewSet, basename="retailchain")
app_name = RetailChainConfig.name

urlpatterns = [] + routers.urls
