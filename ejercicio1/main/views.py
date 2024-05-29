from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Alumno,Genero
from django.db import IntegrityError
from .forms import RegistroForm

# Create your views here.
def home(request):
    return render(request,'Index.html')

def index(request):
    datos = Alumno.objects.all()
    contexto={'alumnos': datos}
    return render(request,'Index.html', contexto)

def addAlumno(request):
    if request.method == 'GET':

        return render(request,'form.html')
    else:                
        print("metodo post ")
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido_paterno = request.POST.get('paterno')
        apellido_materno = request.POST.get('materno')
        fecha_nacimiento = request.POST.get('fechaNAC')
        genero_nombre =request.POST.get('genero')
        telefono =request.POST.get('fono')
        email = request.POST.get('correo')
        direccion =request.POST.get('direccion')
        
        
        genero_obj = Genero.objects.get(genero=genero_nombre)
        
        print(genero_obj)
        
        try:
            alumno = Alumno.objects.create(
                rut=rut,
                nombre=nombre,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                fecha_nacimiento=fecha_nacimiento,
                id_genero=genero_obj,
                telefono=telefono,
                email=email,
                direccion=direccion,
                activo=True
            )
            return render(request, 'form.html')
        except IntegrityError:
            # El correo electrónico ya existe en la base de datos
            error_message = "El correo electrónico ya existe en la base de datos. Por favor, ingresa un correo electrónico diferente."
            return render(request, 'form.html', {'error_message': error_message})
        


def  RegistroAlumno(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario=RegistroForm()
        return render(request,'FormN.html',{'form': formulario})
    

def editar_alumno(request, rut):
    alumno = get_object_or_404(Alumno, rut=rut)
    if request.method == 'POST':
        formulario = RegistroForm(request.POST, instance=alumno)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario=RegistroForm(instance=alumno)
        return render(request,'editar_alumno.html',{'form': formulario})
    