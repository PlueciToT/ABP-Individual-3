from django.urls import path
from . import views
from .views import userlist


urlpatterns = [
path('', views.index, name='index'),
path('users/', userlist, name='userlist'),
path('register/', views.register, name='register'),
]