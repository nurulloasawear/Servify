from rest_framework import viewsets
from admin_logs.models import AdminLog
from .serializers import AdminSerializer
from api.permissions import *
class AdminLogViewSet(viewsets.ModelViewSet):
	queryset = AdminLog.objects.all()
	serializer_class = AdminSerializer
	permission_classes =[IsAdminOrReadOnly,]
	