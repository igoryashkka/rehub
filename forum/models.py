from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    is_published  = models.BooleanField()
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    topic =  models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Post by {self.created_by.username} in {self.topic.title}"
