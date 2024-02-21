from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from forum.models import Post,CustomUser
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import *
from django.contrib.auth.views import LoginView
from django.views import View
from django.db.models import Prefetch
from django.views.generic.detail import DetailView
from forum.forms import *
from django.contrib.auth import authenticate, logout,login
from forum.utils import UserMixin

class Home(UserMixin,ListView):
    model = Post
    template_name = 'forum/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_with_users'] = self.get_posts_with_users()
        if self.request.user.id != None:
            context.update(self.get_user_details_by_id(self.request.user.id))
        return context


class Projects(UserMixin,ListView):
    model = Post 
    template_name = 'forum/projects.html'
    context_object_name = 'projects'
    list_colors = ['badge-primary','badge-secondary','badge-success','badge-danger','badge-warning',' badge-info','badge-dark']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        topic_filter = self.request.GET.get('topic_filter')
        if topic_filter:
            topic = Topic.objects.get(title=topic_filter)
            topic_id = topic.id
            print(f"----- {topic_id}")
            if topic_filter:
                queryset = queryset.filter(topic=topic_id)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_with_users'] = self.get_posts_with_users()
        unique_users = {post.title: len(post.users.all()) for post in Post.objects.all()}
        context['unique_users'] = unique_users
        context['topics'] = Topic.objects.all() 
        if self.request.user.id != None:
            context.update(self.get_user_details_by_id(self.request.user.id))
        return context


class ShowProject(UserMixin,DetailView):
    model = Post
    template_name = 'forum/project.html'
    context_object_name = 'project_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_with_users'] = self.get_posts_with_users() 
        if self.request.user.id != None:  
            context.update(self.get_user_details_by_id(self.request.user.id))
        return context


class Users(UserMixin,ListView):
    model = CustomUser
    template_name = 'forum/users.html'
    context_object_name = 'data_users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.id != None:
            context.update(self.get_user_details_by_id(self.request.user.id))
        context['users'] = CustomUser.objects.all()        

        return context
    

class MyProfile(UserMixin,ListView):
    model = CustomUser
    template_name = 'forum/myprofile.html'
    context_object_name = 'data_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.id != None:
            context.update(self.get_user_details_by_id(self.request.user.id))
        return context


class ShowProfile(UserMixin,DetailView):
    model = CustomUser
    template_name = 'forum/profile.html'
    context_object_name = 'profile_data'
       
    def get(self, request, *args, **kwargs):
        user_details = self.get_user_details_by_slug(self.kwargs.get('slug'))
        requested_user = user_details['current_account']

        if requested_user == request.user:
            return redirect('myprofile')
        
        self.object = requested_user
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_photo_profile'] = self.get_user_details_by_slug(self.kwargs.get('slug', None))['current_photo']
        context.update(self.get_user_details_by_slug(self.kwargs.get('slug', None)))

        if self.request.user.id != None:
            context['current_photo'] = self.get_user_details_by_id(self.request.user.id)['current_photo']
        return context


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'forum/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True

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

    
class AddPage(UserMixin,CreateView):
    form_class = AddProjectForm
    template_name = 'forum/addproject.html'
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic_options'] = Topic.objects.all()
        print(f'Topic.objects.all() - {Topic.objects.all()}')
        if self.request.user.id != None:
            context['current_photo'] = self.get_user_details_by_id(self.request.user.id)['current_photo']
        return context



def logout_user(request):
    logout(request)
    return redirect('login')


#@login_required
def about(request):
    return render(request,'forum/about.html', {'title':'Text Title About','list_data':'nonen'})