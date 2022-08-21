from django.shortcuts import render, redirect
from medico.models import Agenda
from django.contrib.messages import constants
from django.contrib import messages
from medico.forms.CadastroForm import RegisterForm
from medico.forms.LoginForm import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views import generic

def home(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        msg = request.POST.get('msg')
        email = request.POST.get('email')
        agenda = request.POST.get('agenda')

        user = Agenda(nome = nome,
                     telefone = telefone,
                     msg = msg,
                     email = email,
                     agenda = agenda)

        user.save()
        messages.add_message(request, constants.SUCCESS, 'Agendamento enviado com sucesso')

    return render(request, template_name='home/home.html')

def cadastro(request):
    registerForm = RegisterForm()
    message = None


    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            # Aqui verificamos se existe usuário ou e-mail com esse cadastro
            verifyUsername = User.objects.filter(username=username).first()
            verifyEmail = User.objects.filter(email=email).first()

            if verifyUsername is not None:
                message = { 'type': 'danger', 'text': 'Já existe um usuário com este username!' }
            elif verifyEmail is not None:
                message = { 'type': 'danger', 'text': 'Já existe um usuário com este e-mail!' }
            else:
                user = User.objects.create_user(username, email, password)
                if user is not None:
                    message = { 'type': 'success', 'text': 'Conta criada com sucesso!' }
                else:
                    message = { 'type': 'danger',  'text': 'Um erro ocorreu ao tentar criar o usuário.' }

    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Login',
        'link_href': '/login'
    }
    return render(request, 'cadastro/cadastro.html', context=context, status=200)


def login_view(request):
    loginForm = LoginForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect("/")
            else:
                message = {
                    'type': 'danger',
                    'text': 'Dados de usuário incorretos'
                }

    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registrar',
        'link_href': '/register'
    }
    return render(request, 'login/login.html',  context=context, status=200 )

def logout_view(request):
    logout(request)
    return redirect('/login')

def pacientes(request):
    return render(request, 'paciente/pacientes.html')

