from django.db import models

from machines.models import Machine


class Command(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    command = models.TextField()
