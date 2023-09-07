# Tercera-pre-entrega-Ibarra
Tercera pre entrega curso CoderHouse

## Showing de la aplicacion (hosting en Azure): 
### <a href="https://app-aburrida.azurewebsites.net/" style="text-align: center;">tercera-pre-entrega-ibarra.azurewebsites.net</a>

## how to use it?:

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
The server is configured to run in production, to change it got to settings.py and set:
```py
    DEBUG = False

```

7. Enjoy the app at Local host: 
```sh 
    127.0.0.1:8501
```


TODO: 

ERD
arreglar el readme
ver urls.py para ver el status 
