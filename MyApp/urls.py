from django.urls import path
from . import views 

urlpatterns = [
    path("" , views.inicio , name="home"),
    path("cursos" , views.cursos, name="cursos"),
    #path("alta_curso/<str:nombre>/<int:comision>" , views.alta_curso),
    path("profesores" , views.profesores , name="profesores"),
    path("alumnos" , views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso" , views.buscar_curso),
    path("buscar", views.buscar),
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"),
    path("editar_curso/<int:id>", views.editar_curso, name="editar_curso"),
    path("editar_curso", views.cursos, name="editar_curso"),

]

