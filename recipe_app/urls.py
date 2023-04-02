from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.all_login, name='login'),
    path('register', views.add, name='register'),
    path('c_profile', views.c_profile, name='c_profile'),
    path('add_recipe', views.add_recipe, name='add_recipe'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)