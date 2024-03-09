from rest_framework.serializers import ModelSerializer
from filmez import models

class FilmesSerializer(ModelSerializer):
    class Meta:
        model = models.Filmes
        fields = '__all__'