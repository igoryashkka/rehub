from django.shortcuts import get_object_or_404
from forum.models import *


class UserMixin:
    def _get_user_details(self, user):
        return {
            'current_account': user,
            'current_photo': user.photo,
            'user_projects': user.user_projects.all(),
            'username': user.username
        }

    def get_user_details_by_id(self, user_identifier):
        user = get_object_or_404(CustomUser, pk=user_identifier)
        return self._get_user_details(user)

    def get_user_details_by_slug(self, user_identifier):
        user = get_object_or_404(CustomUser, username=user_identifier)
        return self._get_user_details(user)
    
    def get_posts_with_users(self):
        print(self.get_queryset())
        return [(post, post.users.all(),post.topic.color if post.topic else None) for post in self.get_queryset()]

