from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from comum.models import Aluno

def index(request):
    return render(request,'home.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        cpf = request.POST['cpf']
        senha = request.POST['password']
        if campo_vazio(nome):
            messages.error(request,'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request,'O campo email não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(cpf):
            messages.error(request, 'O campo cpf não pode ficar em branco')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Usuário já cadastrado')
            return redirect('cadastro')
        if Aluno.objects.filter(cpf=cpf).exists():
            messages.error(request,'CPF já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request,'Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        aluno = Aluno.objects.create(user=user, cpf=cpf)
        aluno.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    else:
        return render(request,'cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request,'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2
