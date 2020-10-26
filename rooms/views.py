from django.shortcuts import render
from django.http import HttpResponse
from rooms.models import Room
from django.forms.models import model_to_dict

def index(request):
    room_data = Room.objects.values()
    print(room_data)
    context = {}
    return render(request, 'index.html', context)