from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Room,Message
from django.contrib import messages
from django.urls import reverse

# Create Room view
@login_required
def CreateRoomView(request):
    """
    This Function is to Handle the room creation
    
    If the room name already exists, an error message is displayed.
    If the room is successfully created, a success message is displayed
    
    
    Returns:
        Redirects to the home page upon successful room creation,
        or renders the home template with error messages if the room creation fails.
    """
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        if room_name:
            try:
                # Check if a room is already exists
                existing_room = Room.objects.get(room_name=room_name)
                messages.error(request, 'Room name already exists. Please try another name.')
            except Room.DoesNotExist:
                # Create the room 
                room = Room(room_name=room_name)
                room.save()
                messages.success(request, 'Room has been created successfully.')
                return redirect(reverse('home'))
            
    return render(request, 'home.html')

#Join in the Room
@login_required
def JoinRoomView(request):
    
    """
    This View Function is handle joinig a room
     
    If the room exists, the user is redirected to the room page.
    If the room doesn't exist, an error message is displayed,
    and the user is redirected to the home page
    
    Returns:
        Redirects to the room page if the room exists,
        or redirects to the home page with an error message if the room doesn't exist.

    """
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        try:
            room = Room.objects.get(room_name=room_name)
        except Room.DoesNotExist:
            # If the room doesn't exist, show an error message and redirect to the home page
            messages.error(request, 'Room does not exist. Please enter a valid room name.')
            return redirect('home')  

        # Redirect to the room
        return redirect('room', room_name=room_name)
    
    # Redirect to home if the request method is not POST
    return redirect('home')


# View function to display messages in a specific room
@login_required
def MessageView(request, room_name):
    
    """
    View function to dispplay message in a specific room
    
    If the room exists, it fetches all messages associated with that room.
    If the room doesn't exist, it displays an error message and redirects to the home page.
    """
    try:
        get_room = Room.objects.get(room_name=room_name)
        get_messages = Message.objects.filter(room=get_room)
    except Room.DoesNotExist:
        messages.error(request, 'Room does not exist.')
        return redirect('home') 
    
    context = {
        "messages": get_messages,
        "user": request.user,
        "room_name": room_name,
        "username": request.user,
    }
    
    return render(request, 'message.html', context)