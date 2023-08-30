from django.shortcuts import render
from MyApp.models import *
from django.template import loader
from django.http import HttpResponse
from MyApp.forms import Curso_form, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings # esto esta bien, pero hay que basarse en la filosofia de least privilege access

# Create your views here.

def inicio(request):

    if request.user.is_authenticated:
        print(f"\n{request.user}\n")
        avatar_url_path = avatar_logic(request)
        return render( request , "padre.html", {"mensaje":request.user.username ,"url": avatar_url_path})
        
    else:
        return render( request , "padre.html")


def cursos(request):
    cursos = Curso.objects.all()

    if request.user.is_authenticated:
        print(f"\n{request.user}\n")
        avatar_url_path = avatar_logic(request)
        return render( request, "cursos.html", {"cursos": cursos, "url": avatar_url_path})        


    return render( request, "cursos.html", {"cursos": cursos})


@login_required
def alta_curso(request, nombre , comision):
    curso = Curso(nombre=nombre , comision=comision)
    curso.save()
    texto = f"Se guardo en el BD el Curso: {curso.nombre} Comision:{curso.comision}"
    return HttpResponse(texto)


def profesores(request):

    print(f"\n{request.user}\n")
    profesores = Profesor.objects.all()

    if request.user.is_authenticated:
        avatar_url_path = avatar_logic(request)
        return render( request, "profesores.html", {"profesores": profesores, "url": avatar_url_path})
    
    else:
        return render( request, "profesores.html", {"profesores": profesores})
    


@login_required
def alumnos(request):
    print(f"\n{request.user}\n")
    alumnos = Alumno.objects.all()

    if request.user.is_authenticated:
        avatar_url_path = avatar_logic(request)
        return render( request, "alumnos.html", {"alumnos": alumnos, "url": avatar_url_path})
    
    else:
        return render( request, "alumnos.html", {"alumnos": alumnos})


@login_required
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

    if request.user.is_authenticated:
        avatar_url_path = avatar_logic(request)
        return render(request, "buscar_curso.html", {'mensaje':request.user.username, "url": avatar_url_path})
    

    return render( request , "buscar_curso.html")


def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
    
@login_required
def eliminar_curso(request, id):

    curso = Curso.objects.get(id=id)
    curso.delete()

    cursos = Curso.objects.all()
    avatar_url_path = avatar_logic(request)

    return render(request, "cursos.html", {"cursos": cursos,'mensaje':request.user.username, "url": avatar_url_path})

@login_required
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

    avatar_url_path = avatar_logic(request)

    return render(request, "editar_curso.html", {'mi_formulario':mi_formlario, "curso": curso,'mensaje':request.user.username, "url": avatar_url_path})


def login_request(request):

    if request.method == "GET" and request.user.is_authenticated:
            avatar_url_path = avatar_logic(request)        
            return render(request, "inicio.html", {"mensaje": f"{request.user.username} !!", "url": avatar_url_path})


    elif request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            user = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")

            # si encontro un usuario en la DB retorna el user object, if not None
            user_obj = authenticate(username= user, password=passw)

            if user_obj:
                # aca creamos la session de usuario, ( imagino que el broweser recibe un token de sesion)
                login(request, user_obj)

                avatar_url_path = avatar_logic(request)

                return render(request, "inicio.html", {"mensaje": f"Bienvenido@ {user} !!", "url": avatar_url_path})
            
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
            return HttpResponse("formato de nuevo usuario invalido, intente de nuevo")
            
    elif request.method == "GET":
        form = UserCreationForm()

        return render(request, "register.html", {"form": form})

@login_required
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


    avatar_url_path = avatar_logic(request)


    return render(request, "editar_perfil.html", {'mensaje':request.user.username, 'miFormulario': miFormulario, "usuario":usuario, "url": avatar_url_path})


def avatar_logic(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    if avatares.count() == 0:
        avatar_url_path = settings.DEFAULT_AVATAR_URL

    else:
        avatar_url_path = avatares[0].imagen.url

    return avatar_url_path