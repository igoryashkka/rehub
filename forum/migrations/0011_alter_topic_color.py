# Generated by Django 4.2.10 on 2024-02-20 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_topic_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
