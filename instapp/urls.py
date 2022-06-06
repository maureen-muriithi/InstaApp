from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.display_posts, name='posts'),
    path('profile/<username>/', views.profile, name='profile'),
    path('search/', views.search_profile, name='search'),
    path('post/<id>', views.add_comment, name='comment'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)