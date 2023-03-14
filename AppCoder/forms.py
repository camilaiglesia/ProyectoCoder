from django import forms 

class CursoForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)
    camada = forms.IntegerField(min_value=1000)  #min_value: valor minimo que puede tener en la camada

class BusquedaCursoForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)