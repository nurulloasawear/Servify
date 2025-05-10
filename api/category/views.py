from rest_framework import viewsets
from category.models import Category
from .serializers import * 
from api.permissions import IsAdminOrReadOnly
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly)


