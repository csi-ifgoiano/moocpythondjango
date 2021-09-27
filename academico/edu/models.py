from django.db import models
from django.conf import settings
#from comum.models import

# Create your models here.
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
    #TODO
    #cadastrar coordenador
    #coordenador = models.ForeignKeyPlus('comum.Pessoas', null=True, blank=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ('-ativo',)
        app_label = 'edu'

    def __str__(self):
        codigo = self.codigo.replace('-', '')
        return '{} - {}'.format(codigo, self.descricao)