# Generated by Django 4.0.2 on 2023-02-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_blog_banner_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Course title'),
        ),
    ]