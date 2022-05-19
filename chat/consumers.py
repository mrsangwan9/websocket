# every websocket need a consumer for handle connection 
from channels.consumer import SyncConsumer, AsyncConsumer # to make custome consumer we have to extends or inherit these class 
from channels.exceptions import StopConsumer # if any error occur
from time import sleep # import sleep for stop process for one second or as sleep passing time
import asyncio # use sleep time in asyncoConsumer we have to use asyncio.sleep(time in second )
from asgiref.sync import async_to_sync
from .models import chat, Group
import json


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):# this  occur when websocket.connect event happen after open websocket by js
        print('websocket connected...',event)
        print("channel layer", self.channel_layer) #get deafult channel layer from a project
        print("channel name", self.channel_name)# get unqiue channel name
        self.room_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(
           self.room_name,self.channel_name
        )
        self.send({
            'type':'websocket.accept'
        })
      
    def websocket_receive(self,event): # that function run after receive data from the client like message somethin
       
        print("text message received from client...", event['text'])# print message receive from
        print(type(event['text']))
        #find group objects
        groupname = Group.objects.get(name = self.room_name)
       # save client message into database with given user name
        chatt = chat(
            message = event['text'],
            Group_name = groupname
        )
        chatt.save()
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,{
         
            'type':'chat.message',
            'message':event['text'] ,
            
        })

    
    def chat_message(self,event):
        print('event..',event)
        # for i in range(15):
        self.send({
                    "type":"websocket.send",# send data to client
                    'text':event['message']# send i value to client // data must be a string..
                })
        #     sleep(1) # timer for repeate message after interval of time

    def websocket_disconnect(self,event):
        print("connection is disconnect...", event)
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,self.channel_name
        )
        raise StopConsumer
        
















class MyAsyncConsumer(AsyncConsumer):
        async def websocket_connect(self,event):
            print('websocket connected...',event)
            await self.send({
                'type':'websocket.accpet',
            })

        async  def websocket_receive(self,event):
         print("message received from client", event['text'])
         print(event['text'])
         for i in range(15):
            await self.send({
                "type":"websocket.send",
                'text':str(i) 
             })
         asyncio.sleep(1)

        async def websocket_disconnect(self,event):
          print("connection is disconnect")
          raise StopConsumer