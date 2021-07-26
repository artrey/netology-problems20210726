# Generated by Django 3.2.5 on 2021-07-26 16:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_solution_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworktask',
            name='users',
            field=models.ManyToManyField(related_name='tasks', through='courses.Solution', to=settings.AUTH_USER_MODEL),
        ),
    ]
