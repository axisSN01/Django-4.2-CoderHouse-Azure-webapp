from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView, redirect_to_login

urlpatterns = [
    path("" , views.inicio , name="home"), # listo
    path("cursos" , views.cursos, name="cursos"), # listo
    path("profesores" , views.profesores , name="profesores"), 
    path("alumnos" , views.alumnos , name="alumnos"), # listo  
    path("alta_curso", views.curso_formulario, name="alta_curso"), #listo
    path("buscar_curso" , views.buscar_curso, name="buscar_curso"), # listo
    path("buscar", views.buscar), # listo
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"), # listo
    path("editar_curso/<int:id>", views.editar_curso, name="editar_curso"), # listo
    path("editar_curso", views.cursos, name="editar_curso"), # listo
    path("login", views.login_request, name="login"), # listo
    path("register", views.register, name="register"), # listo
    # agregamos una view de tipo clase, se encarga de destruir la sesion. Y borra el token del client browser
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"), # listo
    path("editar_perfil", views.editar_perfil, name='editar_perfil'), # listo
    path("editar_alumno_usuario/<int:id>", views.editar_alumno_usuario, name='editar_alumno_usuario'), # listo 
    path("asignar_alumno_a_usuario/<int:id>", views.asignar_alumno_a_usuario, name='asignar_alumno_a_usuario'),
    path("borrar_alumno/<int:id>", views.borrar_alumno, name='borrar_alumno'),   
]

