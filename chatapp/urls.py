from .views import CreateRoomView,MessageView
from django.urls import path



urlpatterns = [
    path('create_room/',CreateRoomView, name='create_room'),
    path('<str:room_name>/<str:username>/', MessageView, name='room')
]
