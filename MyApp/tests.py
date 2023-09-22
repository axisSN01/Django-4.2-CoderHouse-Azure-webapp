from django.test import TestCase, Client
from django.urls import reverse
from . import views

class TestAllURLs(TestCase):
    def setUp(self):
        self.client = Client()

    def test_all_urls_return_200(self):
        # Lista de todas las URL que deseas verificar
        url_list = [
            reverse(views.inicio), 
            reverse(views.cursos),
            reverse(views.profesores), 
            #reverse(views.alumnos),  
            #reverse(views.curso_formulario), 
            reverse(views.buscar_curso,), 
            reverse(views.buscar), 
            #reverse(views.eliminar_curso), 
            #reverse(views.editar_curso), 
            reverse(views.cursos), 
            reverse(views.login_request), 
            reverse(views.register),
            reverse("logout"),
            #reverse(views.editar_perfil), 
            #reverse(views.editar_alumno_usuario),
            #reverse(views.asignar_alumno_a_usuario),
            #reverse(views.borrar_alumno),             
 
        ]

        for url in url_list:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"La URL {url} no devuelve un estado 200 OK. Devolvio: {response.status_code}")
