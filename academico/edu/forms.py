from django.http import HttpResponse
from .models import Curso, AlunoMatricula
from django import forms
#from djtools.forms.wizard import FormWizard

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        curso_campus = super(CursoForm, self).save(*args, **kwargs)
        return curso_campus

class AlunoMatriculaForm(forms.ModelForm):

    fieldsets = (
        ('Identificação', {'fields': ('nome', ('cpf',), ('data_nascimento', 'estado_civil', 'sexo'))}),
        (
            'Dados Familiares',
            {
                'fields': (
                    'nome_pai',
                    'nome_mae',
                    'responsavel',
                )
            },
        ),
        ('Endereço', {'fields': ('cep', 'logradouro', 'numero', 'complemento', 'bairro', 'estado', 'cidade',)}),
        ('Contato', {'fields': (('telefone', 'telefone_secundario'),)}),
        ('RG', {'fields': ('numero_rg', 'uf_emissao_rg',)}),
        ('Dados da Matrícula', {'fields': ('periodo', 'data_matricula', 'curso',)}),
    )

    class Meta:
        model = AlunoMatricula
        exclude = ()

        def __init__(self, *args, **kwargs):
            super(AlunoMatriculaForm, self).__init__(*args, **kwargs)
            if self.instance.pk:
                self.initial['nome'] = self.instance.pessoa_fisica.nome
                self.initial['data_nascimento'] = self.instance.pessoa_fisica.data_nascimento
                self.initial['sexo'] = self.instance.pessoa_fisica.sexo
                self.initial['cpf'] = self.instance.pessoa_fisica.cpf
                self.initial['raca'] = self.instance.pessoa_fisica.raca_id