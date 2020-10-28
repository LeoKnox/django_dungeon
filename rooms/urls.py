from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<int:room_id>', views.room, name='room'),
]