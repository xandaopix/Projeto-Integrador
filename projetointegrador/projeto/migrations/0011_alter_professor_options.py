# Generated by Django 4.2.10 on 2024-03-13 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0010_alter_aluno_options_alter_curso_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='professor',
            options={'ordering': ['nome'], 'permissions': [('modificar_disciplinas', 'Modificar Disciplinas')]},
        ),
    ]
