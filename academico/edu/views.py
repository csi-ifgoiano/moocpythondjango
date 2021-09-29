from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Curso, AlunoMatricula
from comum.models import Aluno
from .forms import CursoForm, AlunoMatriculaForm


# Create your views here.

def listar_cursos(request):
    cursos = Curso.objects.filter(ativo=True)
    return render(request, 'cursos.html', {'cursos':cursos})

def cursos_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'curso.html', {'curso': curso})

def efetuar_matricula(request, aluno_id=None):
    title = 'Matrícula Institucional'
    candidato_vaga = None
    initial = None
    alunos = AlunoMatricula.objects.none()
    cpf = request.POST.get('cpf')
    form = AlunoMatriculaForm(request, cpf, data=request.POST or None, initial=initial, files=request.FILES or None)
    if form.is_valid():
        aluno = form.processar()
        return HttpResponse("Dados inseridos com sucesso!")
