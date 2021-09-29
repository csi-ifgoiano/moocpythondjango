from django.contrib import admin
from django.http import HttpResponseRedirect
from .forms import CursoForm, AlunoMatriculaForm
from .models import (
    Curso,
    AlunoMatricula
)
# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'conteudo', 'ativo')
    list_filter = ('ativo', 'descricao', 'periodicidade')
    search_fields = ('descricao', 'codigo')
    list_per_page = 15

    form = CursoForm
    fieldsets = (
        (
            'Identificação',
            {
                'fields': (
                    ('ativo',),
                    ('descricao',),
                    ('ch_total',),
                    ('conteudo',),
                )
            },
        ),
        # ('Dados da Criação', {'fields': ('ano_letivo', 'periodo_letivo', ('data_inicio', 'data_fim'), 'ativo')}),
        # ('Coordenação', {'fields': ('coordenador')}),
        (
            'Dados Gerais',
            {
                'fields': (
                    'codigo',
                    'periodicidade',
                    'ppc',
                    'tipo_hora_aula',
                    'media_aprovacao',
                )
            },
        ),
    )

    def response_add(self, request, obj):
        self.message_user(request, 'Curso cadastrado com sucesso!')
        return HttpResponseRedirect('/edu/curso/{}/'.format(obj.pk))

admin.site.register(Curso, CursoAdmin)

class AlunoMatriculaAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'curso')
    list_filter = ('matricula', 'curso')
    search_fields = ('matricula', 'curso')
    list_per_page = 15
    form = AlunoMatriculaForm
    fieldsets = AlunoMatriculaForm.fieldsets

admin.site.register(AlunoMatricula, AlunoMatriculaAdmin)