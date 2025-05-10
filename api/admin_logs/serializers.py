from rest_framework import serializers
from admin_logs.models import  *
class AdminSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdminLog
		exclude = ['created_at']