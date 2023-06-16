from django.urls import path
from . import views
from .views import lista_usuarios, ProveedorView

urlpatterns = [
    path('', views.mensaje, name='telovendo'), 
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('proveedor/', ProveedorView.as_view(), name='registro_proveedores'),

    path('login/', views.login_page, name='login'),
    path('welcome/', views.welcome_page, name='welcome'),
    path('logout/', views.logout_user, name='logout'),
    # path('logout/', logout_view, name='logout'),
]

