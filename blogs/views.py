from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Post, Category
from .forms import PostForm, SignUpForm

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def home(request):
    posts = Post.objects.all().order_by('-pub_date')[:5]
    context = {'posts': posts}
    return render(request, 'blogs/home.html', context)

def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'blogs/index.html', context)

def posts_index(request, username):
    owner = User.objects.get(username=username)
    posts = Post.objects.filter(owner_id=owner.id).order_by('-pub_date')
    context = {'posts': posts, 'owner': owner}
    return render(request, 'blogs/posts_index.html', context)

def post_view(request, username, post_id):
    owner = User.objects.get(username=username)
    post = Post.objects.get(pk=post_id)
    context = {'post': post, 'owner': owner}
    return render(request, 'blogs/post_view.html', context)

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            form.save_m2m()
            return redirect('post_view', username=post.owner.username, post_id=post.id)
    else:
        form = PostForm()

    return render(request, 'blogs/new_post.html', {'form': form})

class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'