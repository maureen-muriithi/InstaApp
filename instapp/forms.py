from django import forms
from .models import Post, Profile, Comment

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
