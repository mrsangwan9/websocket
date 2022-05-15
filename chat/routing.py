from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path('ws/sc/',consumers.MySyncConsumer.as_asgi()),# this route the connection to mysyncconsumer class into consumers file
    path('ws/ac/',consumers.MyAsyncConsumer.as_asgi()),
    
]