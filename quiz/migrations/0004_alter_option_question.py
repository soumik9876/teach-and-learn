# Generated by Django 4.0.2 on 2022-03-10 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_question_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.question', verbose_name='Question'),
        ),
    ]