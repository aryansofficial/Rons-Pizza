from django.urls import path
from . import views


urlpatterns = [
    path('', views.kitchen, name='kitchen'),
    path('update/<int:id>/<str:status>', views.update, name="update"),
    path('dashboard/', views.dashboard, name="dashboard")
]