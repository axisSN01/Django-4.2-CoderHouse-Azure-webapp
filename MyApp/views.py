from django.shortcuts import render
from MyApp.models import Curso
from django.template import loader
from django.http import HttpResponse
from MyApp.forms import Curso_form
# Create your views here.

def inicio(request):
    return render( request , "padre.html")

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    plantillas = loader.get_template("cursos.html")
    documento = plantillas.render(dicc)
    return HttpResponse(documento)



def alta_curso(request, nombre , comision):
    curso = Curso(nombre=nombre , comision=comision)
    curso.save()
    texto = f"Se guardo en el BD el Curso: {curso.nombre} Comision:{curso.comision}"
    return HttpResponse(texto)




def profesores(request):
    return render( request , "profesores.html")


def alumnos(request):
    return render( request , "alumnos.html")




def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_form( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos['nombre'] , comision=datos['comision'])
            curso.save()
            return render( request , "formulario.html")
    
    
    return render( request , "formulario.html")




def buscar_curso(request):
    return render( request , "buscar_curso.html")




def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
    

def eliminar_curso(request, id):

    curso = Curso.objects.get(id=id)
    curso.delete()

    cursos = Curso.objects.all()

    return render(request, "cursos.html", {"cursos": cursos})


def editar_curso(request, id): 

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formlario = Curso_form(request.POST)

        if mi_formlario.is_valid():
            datos = mi_formlario.cleaned_data
            curso.nombre = datos['nombre']
            curso.comision = datos['comision']
            curso.save()

            cursos = Curso.objects.all()    
            return render(request, "cursos.html", {"cursos": cursos})
        
    else:
        mi_formlario = Curso_form(initial={'nombre': curso.nombre, 'comision': curso.comision})


    return render(request, "editar_curso.html", {'mi_formulario':mi_formlario, "curso": curso})
