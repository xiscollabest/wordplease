from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Post, Category

def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'blogs/index.html', context)

def new_post(request):
    context = {}
    return render(request, 'blogs/new_post.html', context)

def posts_index(request, user_id):
    user = User.objects.get(pk=user_id)
    posts = Post.objects.filter(owner_id=user_id)
    context = {'posts': posts, 'user': user}
    return render(request, 'blogs/posts_index.html', context)    