from django.shortcuts import render
from rooms.models import Room


def index(request):
    room_data = Room.objects.values()
    return render(request, 'room/index.html', {'rooms': room_data})

def room(request, room_id):
    room_data = Room.objects.filter(id=room_id)
    print(room_data)
    return render(request, 'room/room.html', {'room_data': room_data[0]})