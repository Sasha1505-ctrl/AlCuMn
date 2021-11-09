from django.urls import re_path

from ClassHome import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/', consumers.ChatConsumer),
]