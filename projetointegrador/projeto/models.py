from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True, unique=True)
    curso = models.TextField(unique=True)
    class Meta:
        ordering = ['curso']

class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True, unique=True)
    username = models.TextField()
    nome = models.TextField()
    sobrenome = models.TextField()
    email = models.EmailField()
    class Meta:
        ordering = ['nome']
        permissions = [("modificar_disciplinas", "Pode Modificar Disciplinas"),]

class Disciplina(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    nome = models.TextField()
    resumo = models.CharField(max_length=255)
    id_professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='id_prof', blank=True)
    class Meta:
        ordering = ['nome']

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True, unique=True)
    username = models.TextField()
    nome = models.TextField()
    sobrenome = models.TextField()
    email = models.EmailField()
    class Meta:
        ordering = ['nome']

class AlunoFazDisciplina(models.Model):
    id = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='id_al')
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='id_disc_aluno')

class CursoEDisciplina(models.Model):
    id = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='id_cursos')
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='id_disc_curso')

