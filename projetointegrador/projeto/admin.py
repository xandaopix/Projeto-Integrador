from django.contrib import admin
from .models import Curso, Disciplina, Aluno, Professor, CursoEDisciplina, AlunoFazDisciplina
# Register your models here.

admin.site.register(Curso)
admin.site.register(CursoEDisciplina)
admin.site.register(Disciplina)
admin.site.register(Aluno)
admin.site.register(AlunoFazDisciplina)
admin.site.register(Professor)