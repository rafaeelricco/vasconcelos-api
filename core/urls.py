from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
from django.urls import include, path
from products.api.viewsets import ProductViewSet
from consortium.api.viewsets import ConsortiumViewSet
from banners.api.viewsets import BannersViewSet
from parts.api.viewsets import PartsViewSet
from useds.api.viewsets import UsedViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"consortium", ConsortiumViewSet)
router.register(r"banners", BannersViewSet)
router.register(r"parts", PartsViewSet)
router.register(r"used", UsedViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
