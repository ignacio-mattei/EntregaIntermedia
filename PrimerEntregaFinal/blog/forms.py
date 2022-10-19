from unittest.util import _MAX_LENGTH
from django import forms

class FormNoticia(forms.Form):
    titulo = forms.CharField(max_length=30)
    contenido = forms.CharField(widget=forms.Textarea)
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaNoticia(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)

class FormReferencia(forms.Form):
    titulo = forms.CharField(max_length=30)
    link = forms.CharField(widget=forms.Textarea)
    fecha_creacion = forms.DateField(required=False)

class FormPublicacionRedes(forms.Form):
    titulo = forms.CharField(max_length=30)
    redsocial = forms.CharField(widget=forms.Textarea)
    fecha_creacion = forms.DateField(required=False)