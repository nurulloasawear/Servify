from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProffessionViewSet

router = DefaultRouter()
router.register(r'professions', ProffessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
