from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Post, Category

def home(request):
    posts = Post.objects.all().order_by('-pub_date')[:5]
    context = {'posts': posts}
    return render(request, 'blogs/home.html', context)

def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'blogs/index.html', context)

def new_post(request):
    context = {}
    return render(request, 'blogs/new_post.html', context)

def posts_index(request, user_id):
    owner = User.objects.get(pk=user_id)
    posts = Post.objects.filter(owner_id=user_id)
    context = {'posts': posts, 'owner': owner}
    return render(request, 'blogs/posts_index.html', context)

def post_view(request, user_id, post_id):
    owner = User.objects.get(pk=user_id)
    post = Post.objects.get(pk=post_id)
    context = {'post': post, 'owner': owner}
    return render(request, 'blogs/post_view.html', context)