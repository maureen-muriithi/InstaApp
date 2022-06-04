from django.contrib import admin
from .models import Post,Comment

# Register your models here.
admin.site.site_header = 'InstaApp - Administration'
admin.site.register(Post)
admin.site.register(Comment)
