from django.shortcuts import render, redirect
from rooms.models import Room
from rooms.forms import RoomForm


def index(request):
    room_data = Room.objects.values()
    return render(request, 'room/index.html', {'rooms': room_data})

def room(request, room_id):
    room_data = Room.objects.filter(id=room_id)
    print(room_data)
    return render(request, 'room/room.html', {'room_data': room_data[0]})

def create(request):
    context = {}

    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    context['form'] = form
    return render(request, 'room/create.html', context)