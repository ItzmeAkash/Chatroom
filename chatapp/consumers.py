import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import *

class ChatConsumer(AsyncWebsocketConsumer):
    """
    Class For Handling Chat messages
    
    This consumer class handles WebSocket connections, disconnections, and receiving messages.
    
    It also includes methods for sending and creating messages
    """
    async def connect(self):
        """
        Called when the WebSocket Connection is establised
        """
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        
        
    async def disconnect(self, close_code):
        
        """
        Called when a Connection is closed
        
        """
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        
        """
        Called when a message is received from the Websocket
        """
        text_data_json = json.loads(text_data)
        message = text_data_json

        event = {
            'type': 'send_message',
            'message': message,
        }

        await self.channel_layer.group_send(self.room_name, event)
        
    async def send_message(self, event):
        
        """
        Called when a messahe need to be sent to the Websocket
        """
        data = event['message']
        await self.create_message(data=data)


        response_data = {
            'sender': data['sender'],
            'message': data['message'],
           
        }
        await self.send(text_data=json.dumps({'message': response_data}))
        
        
        
        
    @database_sync_to_async
    def create_message(self, data):
        """
        creates a new message and saves it to the database
        """
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        
        if not Message.objects.filter(message=data['message']).exists():
            new_message = Message(room=get_room_by_name, sender=data['sender'], message=data['message'])
            new_message.save()