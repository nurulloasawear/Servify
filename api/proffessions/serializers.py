from rest_framework import serializers
from proffessions.models import *

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proffesions
        fields = '__all__'
