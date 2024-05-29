from django.forms import ModelForm, DateInput
from .models import Alumno 


class RegistroForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['rut','nombre','apellido_paterno','apellido_materno',
                  'fecha_nacimiento','id_genero','telefono','email','direccion']
        widgets = {
            'fecha_nacimiento': DateInput(attrs={'type':'date'})
        }
        