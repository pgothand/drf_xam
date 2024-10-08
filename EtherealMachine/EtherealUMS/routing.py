from django.urls import path
from .consumers import MachineDataConsumer

websocket_urlpatterns = [
    path('ws/machine-data/', MachineDataConsumer.as_asgi()),
]
