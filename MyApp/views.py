from django.shortcuts import render
from MyApp.models import *
from django.template import loader
from django.http import HttpResponse
from MyApp.forms import Curso_form, UserEditForm, CustomUserCreationForm, AlumnoUserEditForm, AsignarAlumnoAUsuarioForm
from django.contrib.auth.forms import AuthenticationForm #, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings # esto esta bien, pero hay que basarse en la filosofia de least privilege access
from avatar.models import *
from django.core.exceptions import PermissionDenied
# Create your views here.

def inicio(request):

    if request.user.is_authenticated:
        print(f"\n{request.user}\n")

        return render( request , "padre.html", {"mensaje":request.user.username})
        
    else:
        return render( request , "padre.html")


def cursos(request):

    if request.method == "POST" and request.user.is_authenticated and "Ver mis cursos" in request.POST:
        
        # Buscame el objeto alumno que se corresponde con este ID de usuario y traeme la comision

        is_alumno_id = Alumno.objects.filter(user__id=request.user.id).exists()
        
        if is_alumno_id:
            ## NOTA IMPORTANTE:  la funcion filter() retorna una LISTA QUERYSET, donde el primer elemento podria ser el objeto buscado.
            ## la funcion GET torna el OBJETO buscado desempaquetado, por lo tanto puedo acceder a los modelos relacionados. por ejemplo comision
           mi_comision_obj = Alumno.objects.get(user__id=request.user.id).comision
        
        else:
            return render( request, "cursos.html")

        # traeme todos los cursos que tenga la comision
        mis_cursos = mi_comision_obj.cursos.all()
    
        return render( request, "cursos.html", {"cursos": mis_cursos}) 
    
    else:
        cursos = Curso.objects.all()
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
        
        return render( request, "profesores.html", {"profesores": profesores})
    
    else:
        return render( request, "profesores.html", {"profesores": profesores})
    


@login_required
def alumnos(request):

    alumnos = Alumno.objects.all()

    # traigo usuarios con id alumno asignado
    lista_id_usuarios_con_alumno = alumnos.exclude(user_id=None).values_list("user_id")

    # traigo los usuario sin alumno asignado
    usuarios_sin_alumno = User.objects.exclude(id__in=lista_id_usuarios_con_alumno)

    # chequeo si el usuario posee Id de alumno
    mi_alumno_existe = alumnos.filter(user__id=request.user.id).exists()

    return render( request, 
                  "alumnos.html", 
                  {
                    "alumnos": alumnos, 
                    "usuarios_sin_alumno": usuarios_sin_alumno,                     
                    "is_staff": request.user.is_staff, 
                    "mi_alumno_existe": mi_alumno_existe
                    }
            )


@login_required
def curso_formulario(request):

    if request.user.is_staff:
        if request.method == "POST":

            mi_formulario = Curso_form( request.POST )

            if mi_formulario.is_valid():
                datos = mi_formulario.cleaned_data
                curso = Curso( nombre=datos['nombre'], comision=datos['comision'])
                curso.save()
                return render( request , "formulario.html")
        
        return render( request , "formulario.html")
    
    else:
        return render( request , "padre.html")


def buscar_curso(request):
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
    

    return render(request, "cursos.html", {"cursos": cursos,'mensaje':request.user.username})

@login_required
def editar_curso(request, id): 

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_form(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            wrong_data = False           

            # Verificar si el id no existe ( Foreign key constrain)
            if not Profesor.objects.filter(id=datos['profesor_id']).exists():

                mi_formulario.add_error('profesor_id', 'Este ID de profesor No existe. Elija otro.')                
                wrong_data = True

            if wrong_data:
                return render(request, "editar_curso.html", {'mi_formulario':mi_formulario, "curso": curso,'mensaje':request.user.username})


            curso.nombre = datos['nombre']
            curso.profesor_id = datos['profesor_id']

            curso.save()

            cursos = Curso.objects.all()    
            return render(request, "cursos.html", {"cursos": cursos})
        
    else:
        mi_formulario = Curso_form(initial={'nombre': curso.nombre, 
                                           'profesor_id': curso.profesor_id,                                           
                                           })

    return render(request, "editar_curso.html", {'mi_formulario':mi_formulario, "curso": curso,'mensaje':request.user.username})


def login_request(request):

    if request.method == "GET" and request.user.is_authenticated:    
            return render(request, "inicio.html", {"mensaje": f"{request.user.username} !!"})


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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Luego el staff debe asignar comision y alumno ID

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return render(request, "registro_exitoso.html", {"form": form})
        
        else:
            return render(request, "register.html", {"form": form})
            
    elif request.method == "GET":
        form = CustomUserCreationForm()

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

    return render(request, "editar_perfil.html", {'mensaje':request.user.username, 'miFormulario': miFormulario, "usuario":usuario})



@login_required
def editar_alumno_usuario(request, id):

    if request.user.is_staff:
        alumno = Alumno.objects.get(id=id)        

    else:
        raise PermissionDenied

    if request.method == "POST":
        miFormulario = AlumnoUserEditForm(request.POST)

        if miFormulario.is_valid():


            ### OJO ACA: este atributo es un DICT y se pasa por referencia (mutable object)
            ## Entonces cuando se aplica el metodo add_error mas abajo, se modifica tambien info implicitamente.
            ## por ese motivo conviene usar COPY()
            info = miFormulario.cleaned_data.copy()
       
            wrong_data = False

            # Verificar si el usuario_id ya está ocupado
            if Alumno.objects.filter(user__id=info["user_id"]).exists() and alumno.user_id != info["user_id"]:
                # El usuario_id ya está ocupado
                miFormulario.add_error('user_id', 'Este ID de usuario ya está ocupado por otro alumno. Elija otro.')
                wrong_data = True

            # Verificar si existe la comision
            if not Comision.objects.filter(id=info["comision_id"]).exists():
                miFormulario.add_error('comision_id', 'No existe esta comision. Elija una existente.')
                wrong_data = True

            # Verificar si el usuario_id no existe ( Foreign key constrain)
            if not Alumno.objects.filter(user__id=info["user_id"]).exists():
                # El usuario_id ya está ocupado
                miFormulario.add_error('user_id', 'Este ID de usuario No existe. Elija otro.')                
                wrong_data = True
            

            if wrong_data:
                return render(request, "editar_alumno.html", {'mensaje':alumno.nombre, 'miFormulario': miFormulario, "alumno":alumno})

            else:
                # pdb.set_trace()
                # El usuario_id está disponible, guardar el alumno
                alumno.nombre = info['nombre']
                alumno.apellido = info["apellido"]
                alumno.comision_id = info["comision_id"]
                alumno.user_id = info["user_id"]     
                alumno.save()
                return render(
                    request, 
                    "padre.html",
                    {
                        "is_success":True,
                        "success_message": "Alumno modificado con exito",
                     }
                    )



    # Crear un diccionario de valores iniciales basados en la información de la solicitud
    initial_data = {
        'nombre': alumno.nombre,
        'apellido': alumno.apellido,
        'comision_id': alumno.comision_id,
        'user_id': alumno.user_id,            
    }
    miFormulario = AlumnoUserEditForm(initial=initial_data)


    return render(request, "editar_alumno.html", {'mensaje':alumno.nombre, 'miFormulario': miFormulario, "alumno":alumno})



@login_required
def asignar_alumno_a_usuario(request, id):

    if request.user.is_staff:
        usuario = User.objects.get(id=id)        

    else:
        raise PermissionDenied

    if request.method == "POST":
        miFormulario = AsignarAlumnoAUsuarioForm(request.POST)

        if miFormulario.is_valid():

            ### OJO ACA: este atributo es un DICT y se pasa por referencia (mutable object)
            ## Entonces cuando se aplica el metodo add_error mas abajo, se modifica tambien info implicitamente.
            ## por ese motivo conviene usar COPY()
            info = miFormulario.cleaned_data.copy()
       
            wrong_data = False

            # Verificar si el alumno_id ya está ocupado
            if Alumno.objects.filter(id=info["alumno_id"]).exists():
                # El alumno id ya está ocupado
                miFormulario.add_error('alumno_id', 'Este ID de alumno ya está ocupado por otro alumno. Elija otro.')
                wrong_data = True

            # Verificar si existe la comision
            if not Comision.objects.filter(id=info["comision_id"]).exists():
                miFormulario.add_error('comision_id', 'No existe esta comision. Elija una existente.')
                wrong_data = True
            
            # nos se chequea si el usuario id ya existe en tabla alumno, porque ya se llego a esta vista

            if wrong_data:
                return render(request, "asignar_alumno.html", {'mensaje':usuario.username, 'miFormulario': miFormulario, "usuario":usuario})

            else:
                # pdb.set_trace()
                # El alumno_id está disponible, guardar el id alumno
                # la comision existe y esta disponible

                ### NOTA IMPORTANTE: Django no permite pasar la clase del modelo como argumento de otro modelo. Primero debe ser instanciado. 
                ## por ejemplo, esto falla: 
                # nuevo_alumno = Alumno(
                #     nombre=info['nombre'],
                #     apellido=info["apellido"],
                #     comision=Comision.objects.get(id=info["comision_id"]),
                #     user=usuario,
                # )

                comision_a_asignar = Comision.objects.get(id=info["comision_id"])
                
                nuevo_alumno = Alumno(
                    nombre=info['nombre'],
                    apellido=info["apellido"],
                    comision=comision_a_asignar,
                    user=usuario,
                )

                nuevo_alumno.save()
                return render(
                    request, 
                    "padre.html",
                    {
                        "is_success":True,
                        "success_message": f"Alumno asginado con exito a usuario: {usuario.username}",
                     }
                    )


    # Crear un diccionario de valores iniciales basados en la información de la solicitud
    initial_data = {
        'nombre': usuario.first_name,
        'apellido': usuario.last_name,
        'comision_id': "",
        'alumno_id': "",            
    }
    miFormulario = AsignarAlumnoAUsuarioForm(initial=initial_data)


    return render(request, "asignar_alumno.html", {'mensaje':usuario.username, 'miFormulario': miFormulario, "usuario":usuario})


@login_required
def borrar_alumno(request, id):

    if request.user.is_staff:

        alumno = Alumno.objects.get(id=id)  

        usuario = alumno.user

        alumno.delete()
        
        return render(
                request, 
                "padre.html",
                {
                    "is_success":True,
                    "success_message": f"Alumno Borrado con exito a usuario: {usuario.username}",
                    }
                )

    else:
        raise PermissionDenied
