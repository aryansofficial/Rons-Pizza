from django.urls import path
from . import views

urlpatterns = [
    # data = {}
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register")
]
