from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def userlist(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
