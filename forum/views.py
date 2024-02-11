from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from forum.models import Post,CustomUser
from django.contrib.auth.models import User
# Create your views here.

projects = list(range(1,11))

class Home(ListView):
    model = Post
    template_name = 'forum/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_with_users'] = [(post, post.users.all()) for post in context['posts']]

        users = CustomUser.objects.all()
        for user in users:
            print(f"Projects for user {user.username}: {[project.title for project in user.user_projects.all()]}")


        
        for post in context['posts']:
            print(f"Users for post '{post.title}': {[user.username for user in post.users.all()]}")

        return context

class Projects(ListView):
    model = Post 
    template_name = 'forum/projects.html'
    context_object_name = 'projects'
    
   

def about(request):
    return render(request,'forum/about.html', {'title':'Text Title About','list_data':'nonen'})

