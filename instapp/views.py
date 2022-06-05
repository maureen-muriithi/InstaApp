from django.shortcuts import render, redirect
from django.views.generic.list import ListView
import datetime as dt
from .models import Post, Profile
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User



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
    return render(request, 'insta/post.html', {"date": date,"posts":posts,})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = User.objects.get(username=username)
    if not user:
        return redirect('home')

    profile = Profile.objects.get(user=user)
    args = {
        'username': username,
        'user': user,
        'profile': profile
    }
    print(profile.user.username)
    print(profile.image)
    return render(request, 'insta/profile.html', args)

@login_required(login_url='/accounts/login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        search_results = Profile.search_profile(name)
        print(search_results)
        message = f'name'
        params = {
            'search_results': search_results,
            'message': message
        }
        return render(request, 'insta/search_results.html', params)
    else:
        message = "You haven't searched for any existing profile"
    return render(request, 'insta/search_results.html', {'message': message})

