from django.http import HttpResponse
from django.template import Template,Context,loader



def test_template(request):
    datos = {"nombre":"Pepe" , "notas":[3,6,10,6,5,8,3,7,2,1,10,1]}
    plantilla = loader.get_template("template.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)





""""
def test_template(request):
    
  
    mi_html = open("C:/Users/Maximiliano/Desktop/py/clase18/Proyecto1/Proyecto1/plantillas/template.html")

    plantilla = Template( mi_html.read() )

    mi_html.close()
  
    mi_contexto = Context({"nombre":"Pepe" , "notas":[3,6,10,6,5,8,3,7,2,1,10,1]})


    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
"""