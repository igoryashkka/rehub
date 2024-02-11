from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from forum.models import Post
# Create your views here.

projects = list(range(1,11))

class Home(ListView):
    model = Post
    template_name = 'forum/index.html'
    context_object_name = 'records'
    
    #manage data dynamic 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context


class Projects(ListView):
    model = Post 
    template_name = 'forum/projects.html'
    context_object_name = 'records'
    extra_context = {'projects':projects}# extra_context - only for static data

def about(request):
    return render(request,'forum/about.html', {'title':'Text Title About','list_data':'nonen'})

