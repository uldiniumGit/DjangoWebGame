from django.db import models

# Create your models here.


class PatchNote(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField()


