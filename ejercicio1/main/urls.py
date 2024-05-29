from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='inicio'),
    path('form',views.addAlumno, name='Registrar'),
    path('formulario2',views.RegistroAlumno, name='Registro2'),
    path('editar_alumno/<str:rut>/', views.editar_alumno, name='editar_alumno'),
]