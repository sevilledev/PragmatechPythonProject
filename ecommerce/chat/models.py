from re import X
from django.db import models
from backend.models import User

# Create your models here.

class Room(models.Model):
    users = models.ManyToManyField(User)

class Chat(models.Model):
    message = models.TextField()

    def __str__(self):
        return str(self.id)