# Generated by Django 4.0.2 on 2022-03-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_video_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, verbose_name='Video description'),
        ),
    ]
