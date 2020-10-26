from django.shortcuts import render
from django.http import HttpResponse
from rooms.models import Room

def index(request):
    context = Room.objects.all()
    return render(request, 'index.html', {})