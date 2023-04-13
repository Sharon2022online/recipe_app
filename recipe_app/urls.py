from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('login', views.all_login, name='login'),
    path('user_home', views.user_home, name='user_home'),
    path('register', views.add, name='register'),
    path('c_profile', views.c_profile, name='c_profile'),
    path('add_recipe', views.add_recipe, name='add_recipe'),
    path('edit_recipe', views.edit_recipe, name='edit_recipe'),
    path('view_recipe', views.view_recipe, name='view_recipe'),
    path('edit_profile', views.edit_profile, name='edit_profile'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)