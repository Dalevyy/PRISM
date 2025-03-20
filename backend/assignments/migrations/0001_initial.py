# Generated by Django 5.1.5 on 2025-02-25 03:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('codeGrade_id', models.IntegerField(unique=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_number', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('class_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.class')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.professor')),
            ],
            options={
                'unique_together': {('class_instance', 'assignment_number')},
            },
        ),
        migrations.CreateModel(
            name='FlaggedStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times_over_threshold', models.IntegerField(default=0)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.professor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.student')),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmedCheater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed_date', models.DateField(auto_now_add=True)),
                ('threshold_used', models.IntegerField(default=40)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.professor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.student')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('created_at', models.DateField(auto_now_add=True)),
                ('flagged', models.BooleanField(default=False)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.assignment')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.professor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.student')),
            ],
        ),
        migrations.CreateModel(
            name='FlaggedSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('percentage', models.IntegerField(validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(100)])),
                ('similarity_with', models.ManyToManyField(related_name='similar_submissions', to='assignments.student')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.submission')),
            ],
        ),
    ]
