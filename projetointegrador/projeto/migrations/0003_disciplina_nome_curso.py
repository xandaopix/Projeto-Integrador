# Generated by Django 4.2.10 on 2024-03-01 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0002_disciplina_id_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='nome_curso',
            field=models.CharField(max_length=255, null=True),
        ),
    ]