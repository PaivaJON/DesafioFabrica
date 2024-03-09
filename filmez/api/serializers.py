from rest_framework import serializers
from filmez import models

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filmes
        fields = '__all__'