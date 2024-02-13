from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from forum.models import Post,CustomUser
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from forum.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import CustomUserCreationForm
from django.db.models import Prefetch
from django.views.generic.detail import DetailView
from forum.forms import *

from django.contrib.auth import authenticate, logout,login

# Create your views here.

projects = list(range(1,11))
class Home(ListView):
    model = Post
    template_name = 'forum/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Using prefetch_related for efficient querying
        posts_with_users = Post.objects.prefetch_related(
            Prefetch('users', queryset=CustomUser.objects.all())
        )

        context['posts_with_users'] = [(post, post.users.all()) for post in posts_with_users]

        current_user_id = self.request.user.id
        try:
            current_account = CustomUser.objects.get(pk=current_user_id)
            context['current_account_photo'] = current_account.photo

            # Printing current account photo URL for debugging
            print(f"Current account photo URL: {current_account.photo.url if current_account.photo else 'No photo'}")
        except CustomUser.DoesNotExist:
            context['current_account_photo'] = None
            #print("Current user does not exist")

        # Optimize the user projects query
        users = CustomUser.objects.prefetch_related('user_projects').all()
        for user in users:
            #print(f"Projects for user {user.username}: {[project.title for project in user.user_projects.all()]}")
            pass

        return context
    

class Users(ListView):
    model = CustomUser
    template_name = 'forum/users.html'
    context_object_name = 'data_users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_user_id = self.request.user.id
        current_account = CustomUser.objects.get(pk=current_user_id)

        context['current_account'] = current_account
        context['current_account_photo'] = current_account.photo

        context['users'] = CustomUser.objects.all()
        

        return context

class Projects(ListView):
    model = Post 
    template_name = 'forum/projects.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        posts_with_users = Post.objects.prefetch_related(
            Prefetch('users', queryset=CustomUser.objects.all())
        )

        context['posts_with_users'] = [(post, post.users.all()) for post in posts_with_users]

        unique_users = dict()
        
        posts = Post.objects.all()
        for post in posts:
            for user in post.users.all():
                if len(post.users.all()) > 3:
                    unique_users[post.title] = len(post.users.all()) - 3
                else:
                    unique_users[post.title] = len(post.users.all())


                #print(f"uSER:{user}")
                #print()

        print(unique_users)
        context['unique_users'] = unique_users
        
        

        current_user_id = self.request.user.id

        try:
            current_account = CustomUser.objects.get(pk=current_user_id)
            context['current_account_photo'] = current_account.photo

            # Printing current account photo URL for debugging
            print(f"Current account photo URL: {current_account.photo.url if current_account.photo else 'No photo'}")
        except CustomUser.DoesNotExist:
            context['current_account_photo'] = None
            print("Current user does not exist")
        

        return context
    

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'forum/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'forum/register.html', {'form': form})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'forum/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class ShowProject(DetailView): 
    model = Post
    template_name = 'forum/project.html'
    context_object_name = 'project_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        posts_with_users = Post.objects.prefetch_related(
            Prefetch('users', queryset=CustomUser.objects.all())
        )
        
        context['posts_with_users'] = [(post, post.users.all()) for post in posts_with_users]

        current_user_id = self.request.user.id

        try:
            current_account = CustomUser.objects.get(pk=current_user_id)
            context['current_account_photo'] = current_account.photo

            # Printing current account photo URL for debugging
            print(f"Current account photo URL: {current_account.photo.url if current_account.photo else 'No photo'}")
        except CustomUser.DoesNotExist:
            context['current_account_photo'] = None
            print("Current user does not exist")
        

        return context

class MyProfile(ListView):
    model = CustomUser
    template_name ='forum/myprofile.html'
    context_object_name = 'data_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user_id = self.request.user.id
        for e in CustomUser.objects.all():
            print(e.slug)

        current_account = CustomUser.objects.get(pk=current_user_id)

        context['current_account'] = current_account
        context['current_account_photo'] = current_account.photo

        print(current_account.__dict__)

        users = CustomUser.objects.prefetch_related('user_projects').get(pk=current_user_id)
        #print(f"---{users.user_projects.all()}")
        context['user_projects'] =  users.user_projects.all()
        for user in users.user_projects.all():
            #rint(f"Projects for user {user.username}: {[project.title for project in user.user_projects.all()]}")
            print(user)
            pass


        return context

class ShowProfile(DetailView):
    model = CustomUser
    template_name = 'forum/profile.html'
    context_object_name = 'profile_data'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user_id = self.request.user.id
        current_user_username = self.kwargs.get('slug', None)
        current_account_id = CustomUser.objects.get(pk=current_user_id)

        try:
            current_account = CustomUser.objects.get(username=current_user_username)
            context['current_photo'] = current_account.photo
            context['username'] = current_account.username
            context['current_account'] = current_account
            print(f"log acc {current_account}")
            context['current_account_photo'] = current_account_id.photo


            # Printing current account photo URL for debugging
            print(f"Current account photo URL: {current_account.photo.url if current_account.photo else 'No photo'}")
        except CustomUser.DoesNotExist:
            context['current_photo'] = None
            print("Current user does not exist")

        return context

   

class AddPage(CreateView):
    form_class = AddProjectForm
    template_name = 'forum/addproject.html'
    login_url = '/admin/'

   


def logout_user(request):
    logout(request)
    return redirect('login')

#@login_required
def about(request):
    return render(request,'forum/about.html', {'title':'Text Title About','list_data':'nonen'})

