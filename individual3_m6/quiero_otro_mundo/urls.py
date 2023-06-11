from django.urls import path
from . import views
from .views import userlist, register


urlpatterns = [
path('', views.index, name='index'),
path('users/', userlist, name='userlist'),
path('register/', register, name='register'),
]