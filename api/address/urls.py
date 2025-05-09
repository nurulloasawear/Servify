from django.urls import path
from .views import AddressPkClass,AddressClass
urlpatterns = [
	path('',AddressClass.as_view())
	path('',AddressPkClass.as_view())
]