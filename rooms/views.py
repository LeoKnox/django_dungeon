from django.shortcuts import render
from rooms.models import Room


def index(request):
    room_data = Room.objects.values()
    return render(request, 'room/index.html', {'rooms': room_data})

def room(request):
    return render(request, 'room/room.html', {})