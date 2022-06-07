from django import forms
from .models import Post, Profile, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture', 'bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class NewPostForm(forms.ModelForm):
      class Meta:
        model = Post
        exclude = ['user','likes', 'time_posted']
image = forms.ImageField()
name = forms.CharField(max_length=40)
caption = forms.CharField()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user   
