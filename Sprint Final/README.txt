# ABPro - Sprint Grupal Final Modulo 6

## Aplicación: "Telovendo" 

### Descripción

Mi aplicación "Telovendo" es una aplicación web desarrollada en Django que permite a los usuarios realizar login/logout y ver información sobre los usuarios registrados en la aplicación, 
además de, una vez logueados, ingresar usuarios y ver la info entregada desplegada en la sección "Usuarios registrados" de la aplicación.

### Funcionalidades

- Validación de contraseña mediante Auth de Django.
- Inicio de sesión de usuarios: Si el registro es exitoso, el usuario puede acceder a una página   
   exclusiva (de otro modo inaccesible) con un saludo personalizado con su nombre de usuario.   
  Desde acá el usuario puede volver a "Home" (botón azul), agregar nuevos usuarios (botón verde) o 
  hacer Logout (botón rojo).
- Vista de los últimos usuarios registrados: Visualización de usuarios registrados sin necesidad de
  utilizar el panel de control provisto por Django
- Interfaz intuitiva, minimalista y fácil de usar.

### Grupos de Permisos de Usuarios:

Para revisar los permisos de usuarios es necesario entar a la pagina de administración de Django con las siguientes credenciales:

- Usuario: leorodenas
- Password: leo123465

Los permisos están distribuidos bajos los siguientes grupos:

- Vendedor: A este grupo perteneces los usuarios Peter y Miles, ambos catalogados como Activos y por tanto sin acceso al sitios de Aministración de Django. Ambos solo pueden añadir, 
cambiar y ver usuarios. La intención es restringuir en mayor medida su acceso al sitios para evitar que ambos "vendedores" puedan alterar las tablas extras que no necesiten.
- Administrador: A este grupo pertenecen los usuarios Steve y Antony, ambos catalogados como parte del Staff y por tanto con acceso al sitio de Administración de Django. Los dos tienen todos 
los permisos otorgados a excepción de permisos relacionados a borrar entidades, registros o a manipular el log del proyecto. Además, ellos pueden ver los permisos, grupos y usuarios 
autorizados pero no modificarlos. La intención de estas privaciones es dejar la responsabilidad de borrado en la base de datos y de manipulación del Log como una Actividad exclusiva del 
SuperUser, además de restringir acceso a la tabla de autenticación y evitar que ambos se otorgen a si mismos un estatus más grande (subir a SuperUser). 
- SuperUser: Sólo Leonardo pertenece a este grupo, el cual al tener el status de SuperUser tiene por defecto todos los permisos y por consiguiente no requiere estar en algun grupo en particular 
para obtenerlos (de hay que no aparezca este grupo en la entidad de grupos del panel de administración). Como superUser tiene poder absoluto para ver, modificar, crear y borrar en todas la 
entidades y registros.

### Restricciones

La plicacióon presenta como restricción la imposibilidad de acceder a ciertas páginas (formulario.html e info.html) a menos que el usuario se encuentre autenticado y logueado en la aplicación,
ya que si intenta entrar a ellas desde la barra del navegador (conociendo previamente al dirección), es redireccionado a al sitio de login, para así indicarle que se autentique para poder acceder 
a esos sitios. De la misma manera, en este aspecto el login solo se puede efectuar si el usuario y la contraseña son correctos (registrado previamente el usuario desde el panel de administración 
de Django).

### Requisitos del sistema

- Python 3.11.3
- Django 4.2.1
- DBeaver (o cualquier otro cliente de base de datos que maneje sqlite).
- Navegador web de su preferencia.
- Conexión estable de internet
- dependencias necesarias para la aplicación se encuentran en archivo requirements.txt

### Instrucciones de instalación

1. Clona el repositorio de la aplicación desde GitHub:

   git clone https://github.com/Leonardo-Rodenas/Individuales-Modulo-6

2. Accede al directorio del proyecto:

3. Crea un entorno virtual e instala las dependencias desde requeriments.txt :

   python -m venv (nombre de tu entorno virtual)
   .(nombre de tu entorno virtual)\scripts\activate.bat   <-- Ejecutar dentro del directorio del proyecto
   pip install -r requirements.txt

4. Configura la base de datos:

   - Crea una base de datos en PostgreSQL y actualiza la configuración en el archivo `settings.py`.
   - Si deseas puedes utilzar la base datos por defecto (sqlite3) que trae la aplicación.

5. Aplica las migraciones:

   python manage.py makemigrations
   python manage.py migrate

6. Inicia el servidor local:

   python manage.py runserver

7. Abre tu navegador web y visita `http://localhost:8000` para acceder a la aplicación.

### Soporte

Si tienes alguna pregunta, problema o sugerencia, no dudes en contactarme a través de la sección de "Issues" en GitHub o enviando un correo electrónico a leo.rodenas.e@gmail.com

¡Gracias por utilizar "Telovendo"!
