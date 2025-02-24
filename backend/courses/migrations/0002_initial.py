# Generated by Django 5.1.5 on 2025-02-24 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_professor', to='users.user'),
        ),
        migrations.AddField(
            model_name='professorclasssection',
            name='class_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.class'),
        ),
        migrations.AddField(
            model_name='professorclasssection',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profclassect', to='courses.professor'),
        ),
        migrations.AddField(
            model_name='class',
            name='professors',
            field=models.ManyToManyField(through='courses.ProfessorClassSection', to='courses.professor'),
        ),
        migrations.AddField(
            model_name='professorclasssection',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.semester'),
        ),
    ]
