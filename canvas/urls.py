from django.urls import path

from .consumer import CanvasWebSocketConsumer
from .views import CanvasDetailView, CanvasCreateView

urlpatterns = [
    path('<int:pk>/', CanvasDetailView.as_view(), name='canvas_detail'),
    path('create/', CanvasCreateView.as_view(), name='canvas_create')
]

websocket_urlpatterns = [
    path('ws/canvas/<int:canvas_id>/', CanvasWebSocketConsumer.as_asgi()),
]
