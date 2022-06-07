from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
import datetime as dt
from .models import Post, Profile
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UpdateProfileForm, CommentForm, NewPostForm, RegisterForm



# Create your views here.
@login_required(login_url = "accounts/login")
def index(request):
    date = dt.date.today()
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    form = CommentForm
    args = {
        "date": date,
        "posts": posts,
        "users": users,
        "form" : form
    }
    return render(request, 'insta/index.html', args)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
          user = form.save()
          login(request, user)
          messages.success(request, "Registration successful." )
        return redirect("/login")
    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render(request=request, template_name="django_registration/registration_form.html", context= {'form': form})

def login(request):
  if request.method == "POST":
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
          username = form.cleaned_data.get('username')
          password = form.cleaned_data.get('password')
          user = authenticate(username=username, password=password)
          if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('index/')
          else:
            messages.error(request,"Invalid username or password.")
      else:
          messages.error(request,"Invalid username or password.")
  form = AuthenticationForm()

  return render(request=request, template_name="registration/login.html", context={"form":form})



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
        'profile_form': profile_form,
    }
    print(profile.user.username)
    print(profile.profile_picture)
    return render(request, 'insta/profile.html', args)

def user_profile(request):
    user = request.user
    return render(request, "insta/user_profile.html", {"user":user, "current_user":request.user})  

# def update_profile(request):
     

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
            return redirect("index")
    else:
        form = CommentForm()
        
        args = {
        'post': post,
        'form': form,
    }
    return render(request, 'insta/index.html', args)

@login_required(login_url='accounts/login/')
def add_post(request):
    user = request.user
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = user
            post.save()
            return redirect("index")
    else:
        form = NewPostForm()
        args = {
          "form": form,  
        }

    return render(request, "insta/add_post.html", args)

# def logout_request(request):
#     logout(request)
#     messages.info(request, "You have successfully logged out.") 
#     return render( request, "registration/login.html")


