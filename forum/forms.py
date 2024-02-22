from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import *


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('photo','specialization','telegram','course','description_profile',)

class AddProjectForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['topic'].empty_label = 'Not selected'

    class Meta:
        model = Post
        fields = ['title','description','photo','topic']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-input'}),
            'description': forms.Textarea(attrs={'cols':60,'rows':10}),
        }