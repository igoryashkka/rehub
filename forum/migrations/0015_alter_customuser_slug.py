# Generated by Django 4.2.10 on 2024-02-21 03:28

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='username'),
        ),
    ]
