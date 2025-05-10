from rest_framework import viewsets
from category.models import Category
from .serializers import * 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

