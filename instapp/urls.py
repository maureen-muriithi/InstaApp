from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.display_posts, name='posts'),
    path('profile/<username>/', views.profile, name='profile'),
    path('search/', views.search_results, name='search'),
    path('post/<post_id>', views.add_comment, name='comment'),
    path('newpost', views.add_post, name = "add_post"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)