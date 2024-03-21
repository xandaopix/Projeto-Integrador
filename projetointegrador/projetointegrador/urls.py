from django.contrib import admin
from django.urls import path, include
from projeto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('superuser/', views.superuser, name='superuser'),
    path('superuser/add_disc/', views.add_disc, name='add_disc'),
    path('superuser/add_curso/', views.add_curso, name='add_curso'),
    path('superuser/excluir_curso/<int:id_curso>/', views.excluir_curso, name='excluir_curso'),
    path('superuser/editar_curso/<int:id_curso>/', views.editar_curso, name='editar_curso'),
    path('superuser/excluir_disciplina/<int:id_disciplina>/', views.excluir_disc, name='excluir_disciplina'),
    path('superuser/editar_disciplina/<int:id_disciplina>/', views.editar_disciplina, name='editar_disciplina'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('signup-professor/', views.user_signupprofessor, name='signup-professor'),
    path('', views.base, name='plataforma'),
    path('disciplina/<int:id_disciplina>/', views.disciplina, name='disciplina'),
    path('disciplina/<int:id_disciplina>/add_aluno/', views.add_aluno, name='add_aluno'),
    path('disciplina/excluir_aluno/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
    path('disciplina/editar_aluno/<int:id_aluno>/', views.editar_aluno, name='editar_aluno'),
]
