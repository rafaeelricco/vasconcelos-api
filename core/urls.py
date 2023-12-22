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
from products.api.viewsets import FeaturedViewSet

from categories.api.viewsets import CategoryViewSet
from categories.api.viewsets import CulturesViewSet
from categories.api.viewsets import DisponibilityViewSet
from categories.api.viewsets import FamilyViewSet
from categories.api.viewsets import LaunchViewSet
from categories.api.viewsets import ModelsAndVersionsViewSet
from categories.api.viewsets import SizeOfAreaViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"consortium", ConsortiumViewSet)
router.register(r"banners", BannersViewSet)
router.register(r"parts", PartsViewSet)
router.register(r"used", UsedViewSet)

router.register(r"categories", CategoryViewSet)
router.register(r"cultures", CulturesViewSet)
router.register(r"disponibility", DisponibilityViewSet)
router.register(r"family", FamilyViewSet)
router.register(r"launch", LaunchViewSet)
router.register(r"modelsandversions", ModelsAndVersionsViewSet)
router.register(r"sizeofarea", SizeOfAreaViewSet)
router.register(r'featured', FeaturedViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("admin", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
