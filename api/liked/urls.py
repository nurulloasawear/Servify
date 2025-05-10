from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LikedViewSet as LikedItemViewSet

router = DefaultRouter()
router.register(r'liked', LikedItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
