from django.shortcuts import get_object_or_404
from forum.models import *


class UserMixin:
    def get_user_details(self, user_identifier):
        if isinstance(user_identifier, int):  
            user = get_object_or_404(CustomUser, pk=user_identifier)
        else:
            user = user = get_object_or_404(CustomUser, username=user_identifier)
        return {
            'current_account': user,
            'current_photo': user.photo,
            'user_projects': user.user_projects.all(),
            'username': user.username
        }
    
    def get_posts_with_users(self):
        return [(post, post.users.all()) for post in Post.objects.all()]

