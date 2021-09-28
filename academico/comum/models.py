from django.db import models
from django.contrib.auth.models import Group, User

class Aluno(models.Model):
    sexo_opcoes = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(verbose_name='CPF', max_length=15)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', null=False)
    sexo = models.CharField(choices=sexo_opcoes, max_length=30)
    telefone = models.CharField(verbose_name='Telefone', max_length=15)

    def __str__(self):
        return '{}'.format(self.user.username)


