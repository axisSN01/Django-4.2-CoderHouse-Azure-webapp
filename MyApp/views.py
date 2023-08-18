from django.shortcuts import render
from MyApp.models import Curso
from django.template import loader
from django.http import HttpResponse
from MyApp.forms import Curso_form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login


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
                return render(request, "inicio.html", {"mensaje": f"Bienvenido@ {user} !!"})
            
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
            
    else:
        form = UserCreationForm()

        return render(request, "register.html", {"form": form})

    