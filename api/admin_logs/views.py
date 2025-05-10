from rest_framework import viewsets
from admin_logs.models import AdminLog
from .serializers import AdminSerializer

class AdminLogViewSet(viewsets.ModelViewSet):
	queryset = AdminLog.objects.all()
	serializer_class = AdminSerializer