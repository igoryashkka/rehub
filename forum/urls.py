from django.urls import path 
from .views import *



urlpatterns = [
    path('',Home.as_view(), name = 'home'),
    path('about/',about,name = 'about'),
]