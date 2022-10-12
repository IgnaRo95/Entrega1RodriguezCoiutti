from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class PeliFormu(forms.Form):
    titulo=forms.CharField(max_length=60)
    director=forms.CharField(max_length=60)
    estreno=forms.DateField()
    duracion=forms.IntegerField()
    genero=forms.CharField(max_length=30)


class ActoFormu(forms.Form):
    nombre=forms.CharField(max_length=60)
    nacimiento=forms.DateField()
    sexo=forms.CharField(max_length=10)
    nacionalidad=forms.CharField(max_length=30)
    participo=forms.IntegerField()


class SeriesFormu(forms.Form):
    titulo=forms.CharField(max_length=60)
    director=forms.CharField(max_length=60)
    temporadas=forms.IntegerField()
    episodios=forms.IntegerField()
    emision=forms.DateField()
    continuidad=forms.CharField(max_length=10)


class UserRegisterForm(UserCreationForm):
    username=forms.CharField()
    email=forms.CharField()
    password1=forms.CharField(label='Ingrese Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
        help_text={k:''for k in fields}

class UserEditForm(UserCreationForm):
    username=forms.CharField()
    email=forms.CharField()
    password1=forms.CharField(label='Ingrese Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar nombre')
    last_name=forms.CharField(label='Modificar apellido')
    
    class Meta:
        model=User
        fields=['email', 'password1', 'password2', 'first_name', 'last_name']
        help_text={k:''for k in fields}


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label='Imagen')