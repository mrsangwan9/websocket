# every websocket need a consumer for handle connection 
from channels.consumer import SyncConsumer, AsyncConsumer # to make custome consumer we have to extends or inherit these class 
from channels.exceptions import StopConsumer # if any error occur
from time import sleep # import sleep for stop process for one second or as sleep passing time
import asyncio # use sleep time in asyncoConsumer we have to use asyncio.sleep(time in second )

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connected...',event)
        self.send({
            'type':'websocket.accept',
        })

    def websocket_receive(self,event):
        print("message received from client", ['text'])
        print( ['text'])
        for i in range(15):
            self.send({
                "type":"websocket.send",
                'text':str(i)
             })
            sleep(1)

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