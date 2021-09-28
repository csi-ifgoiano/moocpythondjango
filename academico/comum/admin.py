from django.contrib import admin
from comum.models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('user', 'data_nascimento',)

admin.site.register(Aluno, AlunoAdmin)
