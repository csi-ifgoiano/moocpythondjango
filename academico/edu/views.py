from django.shortcuts import render
from .models import Curso
from django.shortcuts import get_object_or_404
from .forms import CursoForm


# Create your views here.

def listar_cursos(request):
    cursos = Curso.objects.filter(ativo=True)
    return render(request, 'cursos.html', {'cursos':cursos})

def cursos_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'curso.html', {'curso': curso})

def efetuar_matricula(request, cpf_candidado=None):
    title = 'Matrícula Institucional'
    candidato_vaga = None
    initial = None
    #alunos = Aluno.objects.none()
    cpf = request.POST.get('cpf')
    form = EfetuarMatriculaForm(request, cpf, data=request.POST or None, initial=initial, files=request.FILES or None)
    if form.is_valid():
        aluno = form.processar()
    pass