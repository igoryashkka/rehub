from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
#something like project 
class Post(models.Model):
    slug = models.SlugField(max_length = 255, unique = True,db_index = True,verbose_name = 'URL',null=True)
    title = models.CharField(max_length=100)
    status = models.IntegerField(null = True)
    description = models.TextField(null=True)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    is_published  = models.BooleanField()
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='created_posts',null=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_projects')
    topic =  models.ForeignKey(Topic, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"Post by {self.created_by.username} in {self.topic.title}"
    
    def get_absolute_url(self):
        return reverse('project',kwargs={'slug':self.slug})


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    #project = models.ForeignKey(Post, on_delete=models.CASCADE)