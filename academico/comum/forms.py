from django.forms import ModelForm
from comum.models import Aluno
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EditPerfilForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )

class EditAlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ('cpf', 'data_nascimento', 'sexo', 'telefone')
