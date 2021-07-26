from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


class HomeworkTask(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(1)])
    task = models.TextField()
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    users = models.ManyToManyField(
        User,
        related_name='tasks',
        through='Solution',
    )


class Solution(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='solutions',
    )
    homework_task = models.ForeignKey(
        HomeworkTask,
        on_delete=models.CASCADE,
        related_name='solutions',
    )
    text = models.TextField()

    class Meta:
        ordering = ['text']
