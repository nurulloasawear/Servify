from rest_framework import serializers
from Servify.address.models import Address

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = exclude('created_at')