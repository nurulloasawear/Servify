from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet

router = DefaultRouter()
router.register(r'location', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
