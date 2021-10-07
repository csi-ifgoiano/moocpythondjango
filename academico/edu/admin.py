from django.contrib import admin
from django.http import HttpResponseRedirect
from .forms import CursoForm, AlunoMatriculaForm
from .models import Curso, AlunoMatricula

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
                    ('descricao',),
                    ('ch_total',),
                    ('conteudo',),
                )
            },
        ),
        (
            'Dados da Criação',
            {
                'fields': (
                    ('ativo'),
                )
            }
        ),
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
        return HttpResponseRedirect('/cursos/{}/'.format(obj.pk))

admin.site.register(Curso, CursoAdmin)

class AlunoMatriculaAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'curso', 'data_matricula')
    list_filter = ('pessoa_fisica', 'matricula', 'curso')
    search_fields = ('matricula', 'curso')
    list_per_page = 15
    form = AlunoMatriculaForm
    fieldsets = AlunoMatriculaForm.fieldsets

admin.site.register(AlunoMatricula, AlunoMatriculaAdmin)

# class SequencialMatriculaAdmin(admin.ModelAdmin):
#     list_display = ('prefixo', 'contador')
# admin.site.register(SequencialMatricula, SequencialMatriculaAdmin)