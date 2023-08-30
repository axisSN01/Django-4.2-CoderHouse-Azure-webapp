from django.shortcuts import render
from MyApp.models import *
from django.template import loader
from django.http import HttpResponse
from MyApp.forms import Curso_form, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render( request , "padre.html")

# @login_required
# def cursos(request):
#     # arreglar para que reenvie el objeto request, asi se mantiene la sesion
#     cursos = Curso.objects.all()
#     dicc = {"cursos":cursos}
#     plantillas = loader.get_template("cursos.html")
#     documento = plantillas.render(dicc)
#     return HttpResponse(documento)

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    return render( request, "cursos.html", {"cursos": cursos})



def alta_curso(request, nombre , comision):
    curso = Curso(nombre=nombre , comision=comision)
    curso.save()
    texto = f"Se guardo en el BD el Curso: {curso.nombre} Comision:{curso.comision}"
    return HttpResponse(texto)

@login_required
def profesores(request):
    profesores = Profesor.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render( request, "profesores.html", {"profesores": profesores})

@login_required
def alumnos(request):
    print(request.user.id)
    alumnos = Alumno.objects.all()

    if request.user.id != None:
        avatares = Avatar.objects.filter(user=request.user.id)
        return render( request, "alumnos.html", {"alumnos": alumnos, "url": avatares[0].imagen.url})
    
    else:
        return render( request, "alumnos.html", {"alumnos": alumnos})



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


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            user = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")

            # si encontro un usuario en la DB retorna el user object, if not None
            user_obj = authenticate(username= user, password=passw)

            if user_obj:
                # aca creamos la session de usuario, ( imagino que el broweser recibe un token de sesion)
                login(request, user_obj)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request, "inicio.html", {"mensaje": f"Bienvenido@ {user} !!", "url": avatares[0].imagen.url})
            
            # usuerioa object no exite
            else:
                return HttpResponse(f"usuario incorrecto")
            
        # por si el formulario no es valido ( no cumple con requeriminetos de seguridad, por ejemplo)
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")


    # if is not POST, return a clcean form
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Nuevo usuario registrado")
        else:
            return HttpResponse("formato de nuevo usuario invalido")
            
    elif request.method == "GET":
        form = UserCreationForm()

        return render(request, "register.html", {"form": form})


def editar_perfil(request):
    usuario = request.user
    
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            usuario.email = info['email']
            password = info["password1"]
            usuario.set_password(password)
            usuario.save()

            return render(request, "inicio.html")

    else:
        miFormulario = UserEditForm(initial={"email": usuario.email})


    return render(request, "editar_perfil.html", {'miFormulario': miFormulario, "usuario":usuario})

