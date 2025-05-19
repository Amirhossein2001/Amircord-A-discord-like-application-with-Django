from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # Home page at /
    path('room/<str:pk>/', views.room, name='room'),     # Room page at /room/
]
