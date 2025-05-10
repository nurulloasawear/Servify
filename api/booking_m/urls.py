from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BokingViewSets, BokingItemViewSets

router = DefaultRouter()
router.register(r'', BokingViewSets, basename='booking')
router.register(r'item', BokingItemViewSets, basename='booking-item')

urlpatterns = router.urls
