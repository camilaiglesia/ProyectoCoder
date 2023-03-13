from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("cursos", cursos, name="AppCoderCursos"),
    path("estudiantes", estudiantes, name="AppCoderEstudiantes"),
    path("profesores", profesores, name="AppCoderProfesores"),
    path("curso/<nombre>/<camada>", crear_curso,name="AppCoderCurso"),
    
]
