from django.urls import path
from .views import home

urlpatterns = [
    path('pixy/', home, name='pixy'),
]