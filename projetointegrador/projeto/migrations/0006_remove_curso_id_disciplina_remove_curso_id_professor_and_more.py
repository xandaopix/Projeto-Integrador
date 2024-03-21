# Generated by Django 4.2.10 on 2024-03-12 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0005_remove_aluno_email_remove_aluno_id_curso_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='id_disciplina',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='id_professor',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='id_curso',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='nome_curso',
        ),
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='nome',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='sobrenome',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='username',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='username',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='id_professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_prof', to='projeto.professor'),
        ),
    ]