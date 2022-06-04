from django.shortcuts import render
from django.views.generic.list import ListView
import datetime as dt
from .models import Post
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    title = 'Welcome to Instagram'
    return render(request, 'posts/index.html', {"title": title})

@login_required(login_url='/accounts/login/')
def display_posts(request):
    date = dt.date.today()
    posts = Post.objects.all()
    return render(request, 'posts/post.html', {"date": date,"posts":posts,})

