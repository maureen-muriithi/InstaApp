from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
import datetime as dt
from .models import Post, Profile
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import UpdateProfileForm, CommentForm



# Create your views here.
def index(request):
    title = 'Welcome to Instagram'
    return render(request, 'insta/index.html', {"title": title})

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             original_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=original_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = RegisterForm()
#     return render(request, 'django_registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def display_posts(request):
    date = dt.date.today()
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)

    args = {
        "date": date,
        "posts": posts,
        "users": users,
    }
    return render(request, 'insta/post.html', args)

@login_required(login_url='/accounts/login/')
def profile(request, username):
    posts = request.user.profile.posts.all()
    user = User.objects.get(username=username)
    if not user:
        return redirect('home')
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)


    profile = Profile.objects.get(user=user)

    args = {
        'username': username,
        'user': user,
        'profile': profile,
        'posts': posts,
        'profile_form': profile_form,
    }
    print(profile.user.username)
    print(profile.profile_picture)
    return render(request, 'insta/profile.html', args)

@login_required(login_url='/accounts/login')
def search_results(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        searched_results = Profile.search_profile(name)
        print(searched_results)
        message = f'name'
        args = {
            'searched_results': searched_results,
            'message': message
        }
        return render(request, 'insta/search_results.html', args)
    else:
        message = "You haven't searched for any existing profile"
    return render(request, 'insta/search_results.html', {'message': message})

@login_required(login_url='/accounts/login')
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
        args = {
        'post': post,
        'form': form,
    }
    return render(request, 'insta/index.html', args)



