from django.urls import path
from . import views
from .views import userlist


urlpatterns = [
path('', views.index, name='index'),
path('users/', userlist, name='userlist'),
path('register/', views.register, name='register'),
path('login/', views.login_page, name='login'),
path('welcome/', views.welcome_page, name='welcome'),
path('logout/', views.logout_user, name='logout'),
]