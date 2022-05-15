# every websocket need a consumer for handle connection 
from channels.consumer import SyncConsumer, AsyncConsumer # to make custome consumer we have to extends or inherit these class 
from channels.exceptions import StopConsumer # if any error occur
from time import sleep # import sleep for stop process for one second or as sleep passing time
import asyncio # use sleep time in asyncoConsumer we have to use asyncio.sleep(time in second )

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):# this  occur when websocket.connect event happen after open websocket by js
        print('websocket connected...',event)
        self.send({
            'type':'websocket.accept',# websocket connection accept by the server now we can share data both side.
        })

    def websocket_receive(self,event): # that function run after receive data from the client like message somethin
        print("message received from client", ['text']) # print the message.
        print( event['text'])# print message receive from
        for i in range(7):
            self.send({
                "type":"websocket.send",# send data to client
                'text':str(i)# send i value to client // data must be a string..
             })
            sleep(1) # timer for repeate message after interval of time

    def websocket_disconnect(self,event):
        print("connection is disconnect...", event)
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