from .views import CreateRoomView,MessageView,JoinRoomView
from django.urls import path



urlpatterns = [
    path('create_room/',CreateRoomView, name='create_room'),
    path('join_room/',JoinRoomView, name='join_room'),
    path('<str:room_name>', MessageView, name='room')
]