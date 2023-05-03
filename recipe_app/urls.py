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
    path('delete_recipe', views.delete_recipe, name='delete_recipe'),
    path('update_recipe', views.update_recipe, name='update_recipe'),
    path('veg', views.veg, name='veg'),
    path('nonveg', views.nonveg, name='non veg'),
    path('recipe_details', views.recipe_details, name='recipe_details'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('save_recipe', views.save_recipe, name='save_recipe'),
    path('all_recipes', views.all, name='all_recipes'),
    path('add_rating', views.add_rating, name='add_rating'),
    path('favourites', views.favourites, name='favourites'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)