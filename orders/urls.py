from django.urls import path
from . import views


urlpatterns = [
    path('', views.add, name="place_order")
]
