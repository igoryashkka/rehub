# Generated by Django 4.2.10 on 2024-02-21 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_alter_topic_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(null=True),
        ),
    ]
