from django.urls import path 
from .views import *



urlpatterns = [
    path('',Home.as_view(), name = 'home'),
    path('projects/',Projects.as_view(),name = 'about'),
    path('users/',Users.as_view(),name = 'users'),
    path('show_project/<slug:slug>',ShowProject.as_view(),name='project'),
    path('show_profile/<slug:slug>',ShowProfile.as_view(),name='profile'),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('login/',LoginUser.as_view(),name = 'login'),
    path('logout/',logout_user,name = 'logout'),
    path('about/',about,name = 'about'),
    path('addproject/',AddPage.as_view(),name='addproject'),
    path('myprofile/',MyProfile.as_view(),name = 'myprofile')
    
]