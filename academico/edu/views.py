from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CursoForm, AlunoMatriculaForm
from .models import Curso, AlunoMatricula
# from comum.models import Aluno
from django.contrib.auth.models import User


def listar_cursos(request):
    cursos = Curso.objects.filter(ativo=True)
    return render(request, 'cursos.html', {'cursos':cursos})

def cursos_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'curso.html', {'curso': curso})

@login_required()
def efetuar_matricula(request):
    if request.method == 'POST':
        form = AlunoMatriculaForm(request.POST, instance=request.user.aluno)
        curso_id = request.POST.get('curso')
        # aluno = get_object_or_404(Aluno, user=usuario_id)
        aluno_id = request.user.aluno.pk
        if form.is_valid():
            form.processar(aluno_id, curso_id)
            return render(request, 'comprovantematricula.html', {'form':form})
            # return redirect('Aluno com cpf {} matriculado com sucesso!'.format(aluno.cpf))
    else:
        form = AlunoMatriculaForm(instance=request.user.aluno)
    return render(request, 'matricula.html', {'form':form})

@login_required()
def comprovante_matricula(request, pk):
    alunomatricula = get_object_or_404(AlunoMatricula, pk=pk)
    return render(request, 'comprovantematricula.html.html', {'alunomatricula': alunomatricula})

