from django.shortcuts import get_object_or_404, render, redirect
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

def efetuar_matricula(request):
    form = AlunoMatriculaForm()
    return render(request, 'matricula.html', {'form':form})
# def efetuar_matricula(request):
#     title = 'Matrícula Institucional'
#     #curso = get_object_or_404(Curso, pk=curso_id)
#     alunos = AlunoMatricula.objects.none()
#     cpf = request.POST.get('cpf')
#     request.POST.get('')
#     form = AlunoMatriculaForm(data=request.POST or None)
#     if form.is_valid():
#         aluno = form.processar()
#         return redirect('Aluno com cpf {} matriculado com sucesso!'.format(aluno.cpf))
#     return locals()