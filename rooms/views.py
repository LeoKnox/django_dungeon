from django.shortcuts import render
from django.http import HttpResponse
from rooms.models import Room

def index(request):
    room_data = Room.objects.all().values()
    context = {'rooms':room_data}
    print(context)
    return render(request, 'index.html', context)