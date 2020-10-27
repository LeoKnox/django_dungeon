from django.shortcuts import render
from rooms.models import Room


def index(request):
    room_data = Room.objects.values()
    print(room_data)
    return render(request, 'room/index.html', {'rooms': room_data})