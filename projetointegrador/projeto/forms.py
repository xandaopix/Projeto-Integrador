from django import forms 
from .models import Aluno, Professor, Disciplina, Curso, AlunoFazDisciplina
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class AlunoDB(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['username', 'nome', 'sobrenome', 'email']
class ProfessorDB(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['username', 'nome', 'sobrenome', 'email']
class DisciplinaDB(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'resumo', 'id_professor', 'id_disciplina']
class CursoDB(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['curso']
class AlunoFazDisciplinaDB(forms.ModelForm):
    class Meta:
        model = AlunoFazDisciplina
        fields = ['id_aluno', 'id_disciplina']