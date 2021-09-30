from django.db import models
from django.conf import settings
#from djtools.thumbs import ImageWithThumbsField
#from djtools.utils import OverwriteStorage
#from comum.models import

from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal

class Curso(models.Model):
    PERIODICIDADE_ANUAL = 1
    PERIODICIDADE_SEMESTRAL = 2
    PERIODICIDADE_LIVRE = 3
    PERIODICIDADE_CHOICES = [[PERIODICIDADE_ANUAL, 'Anual'], [PERIODICIDADE_SEMESTRAL, 'Semestral'], [PERIODICIDADE_LIVRE, 'Livre']]

    descricao = models.CharField(verbose_name='Descrição', max_length=500)
    ativo = models.BooleanField('Ativo', default=True)
    codigo = models.CharField(verbose_name='Código Matricula', help_text='Código para composição de turmas e matrículas', unique=True, max_length=5)
    ppc = models.FileField(upload_to='static/', null=True, blank=True, verbose_name='PPC', default=None)
    ch_total = models.PositiveIntegerField('Carga Horária Total h/r', blank=True, null=True, default=None)
    tipo_hora_aula = models.PositiveIntegerField('Tipo Hora Aula', blank=True, null=True, choices=[[45, '45 min'], [60, '60 min']])
    periodicidade = models.PositiveIntegerField('Periodicidade', choices=PERIODICIDADE_CHOICES, null=True)
    media_aprovacao = models.DecimalField('Média para aprovação', null=True, blank=True, help_text='Valor entre 0 e 10.',
                          decimal_places=2, max_digits=5, validators=[MinValueValidator(Decimal(0)), MaxValueValidator(Decimal(10))])
    conteudo = models.CharField(verbose_name='Conteúdo', max_length=500, null=True, blank=True)

    #TODO
    #cadastrar coordenador
    #coordenador = models.ForeignKey('comum.Pessoas', null=True, blank=True)
    #cadastrar ano
    #ano_letivo = models.ForeignKey('comum.Ano', verbose_name='Ano letivo', related_name='cursos_por_ano_letivo_set', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ('-ativo',)
        app_label = 'edu'

    def __str__(self):
        codigo = self.codigo.replace('-', '')
        return '{} - {}'.format(codigo, self.descricao)




class AlunoMatricula(models.Model):
    ESTADO_CIVIL_CHOICES = [['Solteiro', 'Solteiro'], ['Casado', 'Casado'], ['União Estável', 'União Estável'], ['Divorciado', 'Divorciado'], ['Viúvo', 'Viúvo']]
    PERIODO_LETIVO_CHOICES = [[1, '1'], [2, '2']]

    # Dados Pessoais
    pessoa_fisica = models.ForeignKey('comum.Aluno', verbose_name='Aluno', related_name='aluno_edu_set', on_delete=models.CASCADE)
    matricula = models.CharField('Matrícula', max_length=255, null=True, blank=True)
    estado_civil = models.CharField(choices=ESTADO_CIVIL_CHOICES, null=True, max_length=20)
    # endereco
    logradouro = models.CharField(max_length=255, verbose_name='Logradouro', null=True)
    numero = models.CharField(max_length=255, verbose_name='Número', null=True)
    complemento = models.CharField(max_length=255, verbose_name='Complemento', null=True, blank=True)
    bairro = models.CharField(max_length=255, verbose_name='Bairro', null=True)
    cep = models.CharField(max_length=255, verbose_name='CEP', null=True, blank=True)
    cidade = models.CharField(max_length=255, verbose_name='Cidade', null=True)
    # dados familiares
    nome_pai = models.CharField(max_length=255, verbose_name='Nome do Pai', null=True, blank=True)
    nome_mae = models.CharField(max_length=255, verbose_name='Nome do Pai', null=True, blank=True)
    responsavel = models.CharField(max_length=255, verbose_name='Nome do Responsável', null=True, blank=True)
    # contato
    telefone_secundario = models.CharField(max_length=15, verbose_name='Telefone Secundário', null=True, blank=True)
    facebook = models.URLField('Facebook', blank=True, null=True)
    instagram = models.URLField('Instagram', blank=True, null=True)
    twitter = models.URLField('Twitter', blank=True, null=True)
    # rg
    numero_rg = models.CharField(max_length=255, verbose_name='Número do RG', null=True, blank=True)
    uf_emissao_rg = models.CharField(max_length=255, verbose_name='Estado Emissor', null=True, blank=True)
    # dados da matrícula
    periodo_letivo = models.PositiveIntegerField(verbose_name='Período de Ingresso', choices=PERIODO_LETIVO_CHOICES)
    data_matricula = models.DateTimeField(verbose_name='Data da Matrícula', auto_now_add=True)
    curso = models.ForeignKey('edu.Curso', verbose_name='Curso', related_name='matricula_edu_set', on_delete=models.CASCADE, default='1')


    # TODO
    #foto = ImageWithThumbsField(storage=OverwriteStorage(), use_id_for_name=True, upload_to='alunos', sizes=((75, 100), (150, 200)), null=True, blank=True) /%d/%m/%Y'
    #ano_letivo = models.ForeignKey('comum.Ano', verbose_name='Ano de Ingresso', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Matricula de Aluno'
        verbose_name_plural = 'Matriculas de Alunos'
        app_label = 'edu'

    def get_nome(self):
        return self.pessoa_fisica.nome


class SequencialMatricula(models.Model):
    prefixo = models.CharField(max_length=255)
    contador = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Sequencial de Matricula'
        verbose_name_plural = 'Sequencial de Matriculas'
        app_label = 'edu'

    @staticmethod
    def proximo_numero(prefixo):
        qs_sequencial = SequencialMatricula.objects.filter(prefixo=prefixo)
        if qs_sequencial.exists():
            sequencial = qs_sequencial[0]
            contador = sequencial.contador
        else:
            sequencial = SequencialMatricula()
            sequencial.prefixo = prefixo
            contador = 1
        sequencial.contador = contador + 1
        sequencial.save()
        numero = '000000000{}'.format(contador)
        matricula = '{}{}'.format(prefixo, numero[-4:])
        if AlunoMatricula.objects.filter(matricula=matricula).exists():
            return SequencialMatricula.proximo_numero(prefixo)
        else:
            return matricula
