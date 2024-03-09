from django.db import models
from uuid import uuid4

# Create your models here.

class Filmes(models.Model):
        id_filmes = models.UUIDField(primary_key = True, default = uuid4, editable = False)
        title = models.CharField(max_length = 255)
        year = models.IntegerField()
        runtime = models.IntegerField()
        genre = models.CharField(max_length = 255)
        director = models.CharField(max_length = 255)