from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Disciplina, Curso, Professor, Aluno, AlunoFazDisciplina
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from .forms import AlunoDB, ProfessorDB, DisciplinaDB, CursoDB, AlunoFazDisciplinaDB

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login_auth(request, user)
            return redirect('plataforma')
        else:
            return HttpResponse('Email ou senha invalidos')
        
def user_signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        username = request.POST.get('username')
        first_name = request.POST.get('nome')
        last_name = request.POST.get('sobrenome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        user = User.objects.filter(username=username, email=email).first()
        if user:
            return HttpResponse("Usuário já cadastrado")
        if password == password2:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            if request.method == 'POST':
                aluno = AlunoDB(request.POST)
                if aluno.is_valid():
                    aluno.save()
                    return redirect('/')
                else:
                    aluno = AlunoDB()
            return render(request, 'login.html')
        return render(request, 'signup.html')
    
def user_signupprofessor(request):
    if request.method == 'GET':
        return render(request, 'signup-professor.html')
    else:
        username = request.POST.get('username')
        first_name = request.POST.get('nome')
        last_name = request.POST.get('sobrenome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        code = request.POST.get('code')

        user = User.objects.filter(username=username, email=email).first()
        if user:
            return HttpResponse("Usuário já cadastrado")
        if code == "1155": #Código de autenticação do professor.
            if password == password2:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, is_superuser=True, password=password)
                user.save()
                if request.method == 'POST':
                    professor = ProfessorDB(request.POST)
                    if professor.is_valid():
                        professor.save()
                        return redirect('/')
                    else:
                        professor = AlunoDB()
                return HttpResponse("Usuário Cadastrado.")
        return render(request, 'signup-professor.html')
    
def user_logout(request):
    logout(request)
    return redirect('login')

@permission_required('projeto.modificar_disciplinas', login_url=('login'))
def superuser(request):
    disciplina = Disciplina.objects.all()
    curso = Curso.objects.all()
    return render(request, 'superuser.html', {'disciplina': disciplina, 'curso': curso})
        
def add_disc(request):
    professor = Professor.objects.all()
    if request.method == 'POST':
        disciplina = DisciplinaDB(request.POST)
        if disciplina.is_valid():
            disciplina.save()
            return redirect('superuser')
        else:
            disciplina = DisciplinaDB()
    return render(request, 'add_disc.html', {'professor':professor})

def add_curso(request):
    if request.method == 'POST':
        curso = CursoDB(request.POST)
        if curso.is_valid():
            curso.save()
            return redirect('superuser')
        else:
            curso = CursoDB()

def add_aluno(request, id_disciplina):
    disciplina = get_object_or_404(Disciplina, id_disciplina=id_disciplina)
    aluno = Aluno.objects.all()
    if request.method == 'POST':
        id_disciplina = request.POST.get('id_disciplina')
        id_aluno = request.POST.get('id_aluno')
        alunoadd = Aluno.objects.get(id_aluno=id_aluno)
        disciplinaadd = Disciplina.objects.get(id_disciplina=id_disciplina)
        alunofaz = AlunoFazDisciplina.objects.create(id_aluno=alunoadd, id_disciplina=disciplinaadd)
        alunofaz.save()
        return redirect('/')
    return render(request, 'add_aluno.html', {'aluno': aluno, 'disciplina': disciplina})

def excluir_aluno(request, id):
    alunofaz = get_object_or_404(AlunoFazDisciplina, id=id)
    if request.method == 'POST':
        alunofaz.delete()
        return redirect('/')
    return render(request, 'confirmar_exclusao.html')

def excluir_curso(request, id_curso):
    curso = get_object_or_404(Curso, id_curso=id_curso)
    if request.method == 'POST':
        curso.delete()
        return redirect('superuser')
    return render(request, 'confirmar_exclusao.html')

def editar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id_curso=id_curso)
    if request.method == 'POST':
        curso = CursoDB(request.POST, instance=curso)
        if curso.is_valid():
            curso.save()
            return redirect('superuser')
        else:
            curso = CursoDB()
    return render(request, 'editar_curso.html', {'curso': curso})

def editar_disciplina(request, id_disciplina):
    disciplina = get_object_or_404(Disciplina, id_disciplina=id_disciplina)
    professor = Professor.objects.all()
    if request.method == 'POST':
        disciplina = DisciplinaDB(request.POST, instance=disciplina)
        if disciplina.is_valid():
            disciplina.save()
            return redirect('superuser')
        else:
            disciplina = DisciplinaDB()
    return render(request, 'editar_disciplina.html', {'disciplina': disciplina, 'professor': professor})

def excluir_disc(request, id_disciplina):
    disciplina = get_object_or_404(Disciplina, id_disciplina=id_disciplina)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('superuser')
    return render(request, 'confirmar_exclusao.html')

@login_required(login_url='login/')
def base(request):
    disciplina = Disciplina.objects.all()
    return render(request, 'home.html', {'disciplina': disciplina})
    
def disciplina(request, id_disciplina):
    disciplina = get_object_or_404(Disciplina, id_disciplina=id_disciplina)
    alunofazdisciplina = AlunoFazDisciplina.objects.all()
    return render(request, 'disciplina.html', {'disciplina': disciplina, 'alunofazdisciplina': alunofazdisciplina})

def editar(request):
    return HttpResponse("Editar dados")

