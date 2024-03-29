# Generated by Django 4.0.2 on 2022-02-26 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_teacher_specialized_in_teacher_user_student_user'),
        ('course', '0002_alter_course_student_alter_course_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, to='accounts.Student', verbose_name='Enrolled students'),
        ),
        migrations.AlterField(
            model_name='video',
            name='watched_by',
            field=models.ManyToManyField(blank=True, to='accounts.Student', verbose_name='Watched by'),
        ),
    ]
