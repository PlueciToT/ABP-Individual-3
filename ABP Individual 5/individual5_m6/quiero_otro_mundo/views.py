from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def is_admin(user):
    return user.is_superuser 

@user_passes_test(is_admin)
def userlist(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # Crea un nuevo usuario
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('index')  # Redirige a la página de registro exitoso
    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            error_message = 'El usuario o contraseña son incorrectos.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

@login_required
def welcome_page(request):
    username = request.user.username
    return render(request, 'welcome.html', {'username': username})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


