# MyApp-Plataforma Cursos - Alexis Ibarra


## Showing de la aplicacion (hosting en Azure): 
### <a href="https://app-aburrida.azurewebsites.net/" style="text-align: center;">app-aburrida.azurewebsites.net</a>


## Schema Entity relational diagram (ERP): 

<img src="https://stacticmedia.blob.core.windows.net/static/MyApp/ERP.svg"  style="height: 600px; width:1000px;"/>

## ScreenCast: 

[ScreenCast-app-aburrida-2023-09-08-16-09-97.webm](https://github.com/axisSN01/Django-CoderHouse/assets/50971046/9a49c5a7-856b-4cc1-a808-20636b9c683c)


## How to testing?: 
| Test | Action                   | Result Expected                                          | Actual Result                                | Check |
|------|--------------------------|----------------------------------------------------------|----------------------------------------------|-------|
| 1    | register user and login  | vista de usuario NO STAFF                                | vista de usuario NO STAFF                    | - [x] |
| 2    | change avatar            | avatar cambiado al perfil                                | avatar cambiado                              | - [x] |
| 3    | Login as ADMIN or STAFF  | vistas de STAFF ( puede borrar y editar cosas)           | vista de staff (puede borrar y editar cosas) | - [x] |
| 4    | asignar usuario a un alumno | logeado como STAFF asignar a alumno un perfil de usuario | perfil asignado                              | - [x] |
| 5    | asignar alumno a usuario  | logeado como STAFF asignar a usuario un alumno id | perfil asignado                              | - [x] |


## Testing sugerido: 

1 - crear usuario no admin 

2 - cambiar el avatar 

3 - ver cursos asignados (/cursos/ "ver mis cursos") (No tendra ningun curso asignado, porque no esta asignado el usuario a un OBJETO ALUMNO)

5 - Ver alumnos (/alumnos) ( muestra BANNER:  "usted no posee un objeto alumno asignado. Solicitar a STAFF" )

7 - Logout 

8 - Login como admin ( perfil STAFF) 

9 - Se habilitan vistas y botones para editar o borrar alumnos, profesores y cursos. 

10 - navegar a alumnos

11- se ven usuario con alumno asignado y usuarios sin alumnos asignados. 

12 - acceder a editar usuario creado en item 1, que no tiene alumno asignado

13 - Asignar alumno y comision a usuario creado en item 1

14 - Logout 

15 - Login con usuario de item 1 y ver cursos asignados (por pertenecer a comision)

16 - fin




## how to run it in local?:

1. Clone the repo
```sh
    git clone https://github.com/axisSN01/Django-CoderHouse.git
``` 
2. Navigate to repo folder
```sh
    cd ./Django-CoderHouse

```

3. Create a virtual enviroment with Python 
```py
    python -m venv venv

```

4. In the same CMD as step 3, activate the virtual enviroment, type:
```sh
    venv\Scripts\activate
```

5. type:  
```py
    pip install -r requirements.txt
```
6. type: 
```py
    python manage.py runserver 8501
```

###  useful note: 
The server is configured to run in production and log into a file (myapp.log), to change it got to settings.py and set:
```py
    DEBUG = True

```

7. Enjoy the app at Local host: 
```sh 
    127.0.0.1:8501
```


