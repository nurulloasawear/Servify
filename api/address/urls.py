from django.urls import path,include
from .views import AddressViewSet
from rest_framework.routers import DefaultRouter
routers = DefaultRouter()
routers.register(r'',AddressViewSet)
urlpatterns = [
	path('',include(routers.urls))
]
