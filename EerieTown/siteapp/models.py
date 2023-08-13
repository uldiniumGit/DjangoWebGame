from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class GameUser(AbstractUser):
    email = models.EmailField(unique=True)

    has_forge_key = models.BooleanField(default=False)
    has_merchant_key = models.BooleanField(default=False)
    has_castle_key = models.BooleanField(default=False)


class PatchNote(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField()


