from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from django.core.asgi import get_asgi_application
import os

import canvas.urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PixelDomination.settings')

django_asgi_app = get_asgi_application()



application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            canvas.urls.websocket_urlpatterns,
        )
    )
})
