from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

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

        return redirect('success')  # Redirige a la página de registro exitoso

    return render(request, 'register.html')