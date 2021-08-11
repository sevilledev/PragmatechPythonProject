from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/(?P<owner>\w+)/(?P<sender>\w+)/$', consumers.ChatConsumer.as_asgi()),
]