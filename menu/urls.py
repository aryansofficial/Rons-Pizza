from django.urls import path, include
from .views import menu
from .views import dish
from .views import search


urlpatterns = [
    path('', menu, name="menu"),
    path('dish/<int:id>', dish, name='dish'),
    path('search/', search, name="search"),
    path('place_order', include('orders.urls'))
]
