
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    '''
    This is equivalent to the image model. Users make posts with images, captions and other things.
    '''
    image = models.ImageField(upload_to = ('posts/'), default="")
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, related_name='posts', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    time_posted = models.DateTimeField(auto_now_add=True, null=True)


    def get_absolute_url(self):
        return reverse('index')

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name
    
    # @classmethod
    # def update_image(cls,current_value,new_value):
    #     updated_image = Post.objects.filter(user=current_value).update(user=new_value)
    #     return updated_image

class Comment(models.Model):
    '''
    This class acts as a model where users can comment on posts
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    time_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'

class Profile(models.Model):
    '''
    Class to display a users profile/details
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' )
    profile_picture = models.ImageField(upload_to='images/', default='default_1.jpg')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
    
    def __str__(self):
        return f'{self.user.username} Profile'


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'


