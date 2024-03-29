# Generated by Django 4.0.2 on 2022-02-20 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('accounts', '0002_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='specialized_in',
            field=models.ManyToManyField(blank=True, null=True, to='course.CourseCategory', verbose_name='Expertise in'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
