from django import forms
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('nombre','apellido','comuna','fecha_nacimiento','correo_electronico','rut','direccion','comuna',)
