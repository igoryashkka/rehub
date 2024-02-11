# Generated by Django 4.2.10 on 2024-02-11 11:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_customuser_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='users',
            field=models.ManyToManyField(related_name='user_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]