import datetime
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from .models import Curso, AlunoMatricula, SequencialMatricula
from comum.models import Aluno
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

    telefone_secundario = forms.CharField(max_length=255, required=False, label='Telefone Secundário', help_text='(XX) XXXX-XXXX')

    logradouro = forms.CharField(max_length=255, required=True, label='Logradouro')
    numero = forms.CharField(max_length=255, required=True, label='Número')
    complemento = forms.CharField(max_length=255, required=False, label='Complemento')
    bairro = forms.CharField(max_length=255, required=True, label='Bairro')
    cidade = forms.CharField(max_length=255, required=True, label='Cidade')
    cep = forms.CharField(max_length=255, required=False, label='Cep')

    nome_pai = forms.CharField(max_length=255, label='Nome do Pai', required=False)
    nome_mae = forms.CharField(max_length=255, label='Nome da Mãe', required=True)
    responsavel = forms.CharField(max_length=255, label='Nome do Responsável', required=False, help_text='Obrigatório para menores de idade.')

    facebook = forms.CharField(max_length=255, label='facebook', required=False)
    instagram = forms.CharField(max_length=255, label='instagram', required=False)
    twitter = forms.CharField(max_length=255, label='twitter', required=False)

    numero_rg = forms.CharField(max_length=255, required=False, label='Número do RG')
    uf_emissao_rg = forms.CharField(max_length=255, required=False, label='Estado Emissor')

    fieldsets = (
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
        ('Endereço', {'fields': ('cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade',)}),
        ('Contato', {'fields': (('telefone_secundario'),)}),
        ('RG', {'fields': ('numero_rg', 'uf_emissao_rg',)}),
        ('Dados da Matrícula', {'fields': ( 'curso',)}),
    )

    class Meta:
        model = AlunoMatricula
        exclude = ('pessoa_fisica', 'matricula',)

        def __init__(self, *args, **kwargs):
            super(AlunoMatriculaForm, self).__init__(*args, **kwargs)
            if self.instance.pk:
                self.initial['nome'] = self.instance.user.nome
                self.initial['data_nascimento'] = self.instance.aluno.data_nascimento
                self.initial['sexo'] = self.instance.aluno.sexo
                self.initial['cpf'] = self.instance.aluno.cpf
                self.initial['telefone'] = self.instance.aluno.telefone

    def processar(self, aluno_id, curso_id):
        aluno = Aluno.objects.get(pk=aluno_id)
        curso = Curso.objects.get(pk=curso_id)

        alunomatricula = AlunoMatricula()
        alunomatricula.estado_civil = self.cleaned_data['estado_civil']
        alunomatricula.pessoa_fisica = aluno
        # endereco
        alunomatricula.logradouro = self.cleaned_data['logradouro']
        alunomatricula.numero = self.cleaned_data['numero']
        alunomatricula.complemento = self.cleaned_data['complemento']
        alunomatricula.bairro = self.cleaned_data['bairro']
        alunomatricula.cep = self.cleaned_data['cep']
        alunomatricula.cidade = self.cleaned_data['cidade']
        # dados familiares
        alunomatricula.nome_pai = self.cleaned_data['nome_pai']
        alunomatricula.nome_mae = self.cleaned_data['nome_mae']
        alunomatricula.responsavel = self.cleaned_data['responsavel']
        # contato
        alunomatricula.telefone_secundario = self.cleaned_data['telefone_secundario']
        alunomatricula.facebook = self.cleaned_data['facebook']
        alunomatricula.instagram = self.cleaned_data['instagram']
        alunomatricula.twitter = self.cleaned_data['twitter']
        # rg
        alunomatricula.numero_rg = self.cleaned_data['numero_rg']
        alunomatricula.uf_emissao_rg = self.cleaned_data['uf_emissao_rg']
        # dados da matrícula
        alunomatricula.periodo_letivo = self.cleaned_data['periodo_letivo']
        # alunomatricula.curso = curso
        alunomatricula.curso = curso
        alunomatricula.save()
        ano_corrente = datetime.date.today().year
        prefixo = '{}{}{}'.format(ano_corrente, alunomatricula.periodo_letivo, curso.codigo)
        alunomatricula.matricula = SequencialMatricula.proximo_numero(prefixo)
        alunomatricula.save()

        return alunomatricula