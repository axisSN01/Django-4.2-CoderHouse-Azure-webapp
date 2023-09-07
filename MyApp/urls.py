from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView, redirect_to_login

urlpatterns = [
    path("" , views.inicio , name="home"), # falta cambiar tamanio banner y color
    path("cursos" , views.cursos, name="cursos"), # falta cambiar estilo botones mis cursos
    path("profesores" , views.profesores , name="profesores"), # no edite profesores, pendiente
    path("alumnos" , views.alumnos , name="alumnos"), # listo  
    path("alta_curso", views.curso_formulario, name="alta_curso"), #listo
    path("buscar_curso" , views.buscar_curso), # listo
    path("buscar", views.buscar), # falta analizar
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"), # falta analizar
    path("editar_curso/<int:id>", views.editar_curso, name="editar_curso"), # falta analizar
    path("editar_curso", views.cursos, name="editar_curso"), # falta analizar
    path("login", views.login_request, name="login"), # listo
    path("register", views.register, name="register"), # listo
    # agregamos una view de tipo clase, se encarga de destruir la sesion. Y borra el token del client browser
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"), # falta redirigir a home + fade banner
    path("editar_perfil", views.editar_perfil, name='editar_perfil'), # falta acomodar botones y edit avatar
    path("editar_alumno_usuario/<int:id>", views.editar_alumno_usuario, name='editar_alumno_usuario'), # no funciona bien el Save()    
    # Falta acomodar las templates de AVATAR, para volver a home 
]

