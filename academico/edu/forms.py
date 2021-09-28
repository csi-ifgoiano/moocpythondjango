from django.http import HttpResponse
from .models import Curso
from django import forms

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        curso_campus = super(CursoForm, self).save(*args, **kwargs)
        return curso_campus