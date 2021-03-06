# Generated by Django 3.2.7 on 2021-09-27 19:02

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=500, verbose_name='Descrição')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('codigo', models.CharField(help_text='Código para composição de turmas e matrículas', max_length=5, unique=True, verbose_name='Código Matricula')),
                ('ppc', models.FileField(blank=True, default=None, null=True, upload_to='static/', verbose_name='PPC')),
                ('ch_total', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Carga Horária Total h/r')),
                ('tipo_hora_aula', models.PositiveIntegerField(blank=True, choices=[[45, '45 min'], [60, '60 min']], null=True, verbose_name='Tipo Hora Aula')),
                ('periodicidade', models.PositiveIntegerField(choices=[[1, 'Anual'], [2, 'Semestral'], [3, 'Livre']], null=True, verbose_name='Periodicidade')),
                ('media_aprovacao', models.DecimalField(blank=True, decimal_places=2, help_text='Valor entre 0 e 10.', max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0')), django.core.validators.MaxValueValidator(Decimal('10'))], verbose_name='Média para aprovação')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ('-ativo',),
            },
        ),
    ]
