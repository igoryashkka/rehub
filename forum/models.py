from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from autoslug import AutoSlugField
# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.title
    
#something like project 
class Post(models.Model):
    slug = AutoSlugField(populate_from='title',null= True)
    title = models.CharField(max_length=100)
    status = models.IntegerField(null = True)
    description = models.TextField(null=True)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    is_published  = models.BooleanField(null = True,default=False)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='created_posts',null=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_projects')
    topic =  models.ForeignKey(Topic, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('project',kwargs={'slug':self.slug})


class CustomUser(AbstractUser):
    slug = AutoSlugField(populate_from='username',null= True)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    specialization = models.CharField(max_length=100,null=True)
    telegram = models.CharField(max_length=100,null=True)
    course = models.IntegerField(null = True)
    description_profile = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse('profile',kwargs={'slug':self.slug})

