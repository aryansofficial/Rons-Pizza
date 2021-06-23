# chat/routing.py
from django.urls import re_path, path

from . import consumer

# websocket_urlpatterns = [
#     re_path(r'ws/order/(?P<order_id>\w+)/$', consumer.ChatConsumer.as_asgi()),
# ]

ws_pattern = [
    path('ws/order/<order_id>',consumer.OrderProgress),
]