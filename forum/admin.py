from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.Topic)
admin.site.register(models.CustomUser)



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_time')
    filter_horizontal = ('users',)  # This provides a user-friendly interface for M2M field

admin.site.register(models.Post, PostAdmin)