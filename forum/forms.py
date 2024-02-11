from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import *



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('photo',)

class AddProjectForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        #self.fields['cat'].empty_label = 'Not selected'
        
    class Meta:
        model = Post
        fields = ['title','slug','description','is_published','photo']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-input'}),
            'description': forms.Textarea(attrs={'cols':60,'rows':10}),
        }