from django.urls import path
from .consumers import ChatConsumer

## Create Path to ChatConsumer
websocket_urlpatterns = [
    path('ws/notification/<str:room_name>/',ChatConsumer.as_asgi())
]