from django.urls import path 
from .views import *



urlpatterns = [
    path('',Home.as_view(), name = 'home'),
    path('projects/',Projects.as_view(),name = 'about'),
    path('about/',about,name = 'about'),
]