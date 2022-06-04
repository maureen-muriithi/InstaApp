
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    '''
    This is equivalent to the image model. Users make posts with images, captions and other things.
    '''
    image = models.ImageField(upload_to = ('images/'), default="")
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    time_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'


