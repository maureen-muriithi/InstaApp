from django import forms
from .models import Profile, Comment

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture', 'bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
