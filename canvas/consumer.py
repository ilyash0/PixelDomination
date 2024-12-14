from json import loads, dumps

from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.timezone import now
from asgiref.sync import sync_to_async

from user.models import CustomUser
from .models import Canvas


class CanvasWebSocketConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name: str = None
        self.canvas_id: int = None
        self.user: CustomUser = None

    async def connect(self):
        self.canvas_id = self.scope['url_route']['kwargs']['canvas_id']
        self.user = self.scope['user']
        self.room_group_name = f'canvas_{self.canvas_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        canvas_state = await self.get_canvas_state(self.canvas_id)
        await self.send(text_data=dumps({
            'canvasState': canvas_state
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = loads(text_data)
        canvas_id = data['canvas_id']
        pixel_data = data['pixelData']
        await self.increment_user_pixel_count(1)

        await self.update_canvas_state(canvas_id, pixel_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'canvas_update',
                'pixelData': pixel_data
            }
        )

    async def canvas_update(self, event):
        pixel_data = event['pixelData']
        await self.send(text_data=dumps({
            'pixelData': pixel_data
        }))

    @sync_to_async
    def get_canvas_state(self, canvas_id):
        canvas = Canvas.objects.get(id=canvas_id)
        return self.transform_record(canvas.state)

    @sync_to_async
    def update_canvas_state(self, canvas_id, pixel_data: dict):
        canvas = Canvas.objects.get(id=canvas_id)
        canvas.state[f'{pixel_data['x']}_{pixel_data['y']}'] = pixel_data['color']
        canvas.updated_at = now()
        canvas.save()

    @sync_to_async
    def increment_user_pixel_count(self, count):
        self.user.pixels_colored += count
        self.user.save()

    @staticmethod
    def transform_record(record):
        result = []
        for key, value in record.items():
            if '_' in key:
                x, y = key.split('_', 1)
                result.append({
                    'x': x,
                    'y': y,
                    'color': value
                })
        return result
