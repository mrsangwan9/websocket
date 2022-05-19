# chat/views.py
from django.shortcuts import render
from .models import chat ,Group

def index(request):
    return render(request, 'chat/home.html', {})

def room(request, room_name):
    groupname= Group.objects.filter(name = room_name).first()
    chats = []
    if groupname:
        chats =chat.objects.filter(Group_name = room_name)
        print(chats)
        return render (request,'chat/room.html',{
            'room_name': room_name,'chats':chats
        })    
    else:
        group = Group(name = room_name)
        group.save()
        return render(request, 'chat/room.html', {
        'room_name': room_name
    })
