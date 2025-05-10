from rest_framework import serializers
from liked.models import LikedAd

class LikedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedAd
        fields = '__all__'
