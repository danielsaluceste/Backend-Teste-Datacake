from django.db import models

# Create your models here.

class todoItem(models.Model):

    tarefa = models.CharField(max_length=60)
    enable = models.BooleanField(default=True)