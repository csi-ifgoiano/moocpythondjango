from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from .models import Curso, AlunoMatricula
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

    nome = forms.CharField(max_length=255, required=True, label='nome')
    cpf = forms.CharField(label='CPF', required=False)
    data_nascimento = forms.DateField()
    sexo = forms.ChoiceField(choices=[['M', 'Masculino'], ['F', 'Feminino'], ['O', 'Outro']])
    telefone = forms.CharField(max_length=255, required=False, label='Telefone Principal', help_text='(XX) XXXX-XXXX')
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
        ('Identificação', {'fields': ('nome', 'cpf', ('data_nascimento', 'estado_civil', 'sexo'))}),
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
        ('Contato', {'fields': (('telefone', 'telefone_secundario'),)}),
        ('RG', {'fields': ('numero_rg', 'uf_emissao_rg',)}),
        ('Dados da Matrícula', {'fields': ( 'curso',)}),
    )

    class Meta:
        model = AlunoMatricula
        exclude = ()

        # def __init__(self, *args, **kwargs):
        #     super(AlunoMatriculaForm, self).__init__(*args, **kwargs)
        #     if self.instance.pk:
        #         self.initial['nome'] = self.instance.pessoa_fisica.nome
        #         self.initial['data_nascimento'] = self.instance.pessoa_fisica.data_nascimento
        #         self.initial['sexo'] = self.instance.pessoa_fisica.sexo
        #         self.initial['cpf'] = self.instance.pessoa_fisica.cpf
        #         self.initial['telefone'] = self.instance.pessoa_fisica.telefone

        def processar(self):
            usuario = User()
            usuario.username = self.cleaned_data['nome']
            usuario.save()

            pessoa_fisica = Aluno()
            pessoa_fisica.cpf = self.cleaned_data['cpf']
            pessoa_fisica.data_nascimento = self.cleaned_data['data_nascimento']
            pessoa_fisica.telefone = self.cleaned_data['telefone']
            pessoa_fisica.sexo = self.cleaned_data['sexo']
            pessoa_fisica.save()

            aluno = AlunoMatricula()
            aluno.estado_civil = self.cleaned_data['estado_civil']
            aluno.pessoa_fisica = pessoa_fisica
            # endereco
            aluno.logradouro = self.cleaned_data['logradouro']
            aluno.numero = self.cleaned_data['numero']
            aluno.complemento = self.cleaned_data['complemento']
            aluno.bairro = self.cleaned_data['bairro']
            aluno.cep = self.cleaned_data['cep']
            aluno.cidade = self.cleaned_data['cidade']
            # dados familiares
            aluno.nome_pai = self.cleaned_data['nome_pai']
            aluno.nome_mae = self.cleaned_data['nome_mae']
            aluno.responsavel = self.cleaned_data['responsavel']
            # contato
            aluno.telefone_secundario = self.cleaned_data['telefone_secundario']
            aluno.facebook = self.cleaned_data['facebook']
            aluno.instagram = self.cleaned_data['instagram']
            aluno.twitter = self.cleaned_data['twitter']
            # rg
            aluno.numero_rg = self.cleaned_data['numero_rg']
            aluno.uf_emissao_rg = self.cleaned_data['uf_emissao_rg']
            # dados da matrícula
            aluno.periodo_letivo = self.cleaned_data['periodo_letivo']
            prefixo = '{}{}{}'.format(aluno.ano_letivo, aluno.periodo_letivo, aluno.curso_campus.codigo)
            aluno.matricula = SequencialMatricula.proximo_numero(prefixo)

            aluno.save()

            return aluno