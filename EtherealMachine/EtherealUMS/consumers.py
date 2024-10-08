from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MachineDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'machine_data'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Broadcast received data to all group members
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'machine_data_message',
                'message': data
            }
        )

    async def machine_data_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
