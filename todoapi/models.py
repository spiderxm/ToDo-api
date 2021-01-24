from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    id = models.CharField(max_length=256, default=uuid4(), primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    end_date = models.DateTimeField(null=False)
    priority = models.CharField(max_length=256, choices=(
        ('Future', 'Future'),
        ('Urgent', 'Urgent'),
        ('Later', 'Later')
    ))
    high_priority = models.BooleanField(default=False)
