from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Room,Message
# Create Room view
@login_required
def CreateRoomView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room_name = request.POST.get('room_name')
        if username and room_name:
            try:
                # Check if the room already exists
                room = Room.objects.get(room_name=room_name)
            except Room.DoesNotExist:
                # If the room doesn't exist, create a new room
                room = Room(room_name=room_name)
                room.save()
            return redirect('room',room_name=room,username = username)
            
    return render(request, 'home.html')

# MessageView
@login_required
def MessageView(request, room_name,username):
    get_room =Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)
    
    context = {
        "messages":get_messages,
        "user":username,
        "room_name":room_name,
    }
    
    return render(request, 'message.html', context)
