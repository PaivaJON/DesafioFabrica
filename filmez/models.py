from django.db import models
from uuid import uuid4

# Create your models here.

class Filmes(models.Model):
        id_filmes = models.UUIDField(primarykey = True, default = uuid4, editable = False)
        title = models.Charfield(max_length = 300)
        year = models.IntegerField()
        runtime = models.IntegerField()
        genre = models.Charfield(max_length = 300)
        director = models.Charfield(max_length = 300)