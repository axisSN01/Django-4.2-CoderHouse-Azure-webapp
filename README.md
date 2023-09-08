# MyApp-Plataforma Cursos - Alexis Ibarra


## Showing de la aplicacion (hosting en Azure): 
### <a href="https://app-aburrida.azurewebsites.net/" style="text-align: center;">tercera-pre-entrega-ibarra.azurewebsites.net</a>


## Schema Entity relational diagram (ERP): 

<img src="https://stacticmedia.blob.core.windows.net/static/MyApp/ERP.svg"  style="height: 600px; width:1000px;"/>



## How to testing?: 
| Test | Action                   | Result Expected                                          | Actual Result                                | Check |
|------|--------------------------|----------------------------------------------------------|----------------------------------------------|-------|
| 1    | register user and login  | vista de usuario NO STAFF                                | vista de usuario NO STAFF                    | - [x] |
| 2    | change avatar            | avatar cambiado al perfil                                | avatar cambiado                              | - [x] |
| 3    | Login as ADMIN or STAFF  | vistas de STAFF ( puede borrar y editar cosas)           | vista de staff (puede borrar y editar cosas) | - [x] |
| 4    | asignar usuario a un alumno | logeado como STAFF asignar a alumno un perfil de usuario | perfil asignado                              | - [x] |
| 5    | asignar alumno a usuario  | logeado como STAFF asignar a usuario un alumno id | perfil asignado                              | - [x] |




## how to run it in local?:

1. Clone the repo
```sh
    git clone https://github.com/axisSN01/Tercera-pre-entrega-Ibarra.git
``` 
2. Navigate to repo folder
```sh
    cd ./Tercera-pre-entrega-Ibarra

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
    DEBUG = False

```

7. Enjoy the app at Local host: 
```sh 
    127.0.0.1:8501
```


