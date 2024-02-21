from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

# Register your models here.


admin.site.register(models.Topic)
admin.site.register(models.Post)



class CustomUserAdmin(admin.ModelAdmin):
    lmodel = models.CustomUser
    list_display = ['username', 'email', 'photo', 'is_staff', ]
    #filter_horizontal = ('users',) 


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(models.CustomUser, CustomUserAdmin)