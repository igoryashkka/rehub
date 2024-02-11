from django.urls import path 
from .views import *



urlpatterns = [
    path('',Home.as_view(), name = 'home'),
    path('projects/',Projects.as_view(),name = 'about'),
    path('show_project/<slug:slug>',ShowProject.as_view(),name='project'),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('login/',LoginUser.as_view(),name = 'login'),
    path('logout/',logout_user,name = 'logout'),
    path('about/',about,name = 'about'),
    path('addproject/',AddPage.as_view(),name='addproject'),
]