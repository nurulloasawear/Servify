from rest_framework import viewsets
from chat_messages.models import ChatMessage
from .serializers import *
class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

