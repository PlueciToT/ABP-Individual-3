from django.shortcuts import redirect, render
from .models import Usuario, proveedor
from .forms import RegistroProveedorForm
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def mensaje(request):
    return render(request, 'index.html')


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

# def registro_proveedor(request):
#     form = RegistroProveedorForm()
#     if request.method == 'POST':
#         form = RegistroProveedorForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index.html')
#     else:
#         form = RegistroProveedorForm()

#     return render(request, 'proveedores.html', {'form': form})


class ProveedorView(TemplateView):
    template_name = 'proveedores.html'

    def get(self, request, *args, **kwargs):
        formulario = RegistroProveedorForm()
        return render(request, self.template_name, {"formulario": formulario})

    def post(self, request, *args, **kwargs):
        formulario = RegistroProveedorForm(request.POST)
        mensajes = {
            "enviado": False,
            "resultado": None
        }
        if formulario.is_valid():
            razon_social = formulario.cleaned_data["razon_social"]
            nombre = formulario.cleaned_data["nombre"]
            rep_legal = formulario.cleaned_data["rep_legal"]
            rut = formulario.cleaned_data["rut"]
            dirección = formulario.cleaned_data["dirección"]
            correo = formulario.cleaned_data["correo"]
            telefono = formulario.cleaned_data["telefono"]
            registro = proveedor(
                razon_social=razon_social,
                nombre=nombre,
                rep_legal=rep_legal,
                rut=rut,
                dirección=dirección,
                correo=correo,
                telefono=telefono,
            )
            registro.save()
            mensajes = {"enviado": True,
                        "resultado": "Mensaje enviado correctamente"}
        else:
            mensajes = {"enviado": False, "resultado": formulario.errors}
        return render(request, self.template_name, {"formulario": formulario, "mensajes": mensajes})

# def logout_view(request):
#   return render(request, "prefil_usuario.html")


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            error_message = 'Su usuario o contraseña son incorrectos'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def welcome_page(request):
    username = request.user.username
    return render(request, 'welcome.html', {'username': username})
