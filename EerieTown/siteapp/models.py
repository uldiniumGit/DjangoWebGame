from django.db import models
from django.contrib.auth.models import AbstractUser

class GameUser(AbstractUser):
    email = models.EmailField(unique=True)

    has_forge_key = models.BooleanField(default=False)
    has_greenhouse_key = models.BooleanField(default=False)
    has_stones_key = models.BooleanField(default=False)
    has_loft_key = models.BooleanField(default=False)
    has_kitchen_key = models.BooleanField(default=False)
    has_fisherman_key = models.BooleanField(default=False)
    day_two = models.BooleanField(default=False)
    day_three = models.BooleanField(default=False)
    end = models.BooleanField(default=False)


class PatchNote(models.Model):
    name = models.CharField(max_length=50, unique=True)  # увеличил длину с 16 до 50
    description = models.TextField(blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
