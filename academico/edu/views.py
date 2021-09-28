from django.shortcuts import render
from .models import Curso
from .forms import CursoForm


# Create your views here.

def listar_cursos(request):
    cursos = Curso.objects.filter(ativo=True)
    return render(request, 'curso.html', {'cursos':cursos})


