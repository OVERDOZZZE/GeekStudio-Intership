from rest_framework import serializers, status
from rest_framework.relations import StringRelatedField
from user.serializers import UserSerializer
from .models import Manga, Genre, Review
from user.models import CustomUser


class ReviewSerializer(serializers.ModelSerializer):
    author = StringRelatedField(read_only=True)
    nickname = serializers.CharField(source='author.nickname', read_only=True)

    class Meta:
        model = Review
        fields = 'id text author nickname post'.split()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'slug', 'name']


class MangaSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        model = Manga
        fields = 'id title description type genre slug publication_year image'.split()


