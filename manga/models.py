from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from multiselectfield import MultiSelectField

from user.models import CustomUser


class Genre(models.Model):
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    name = models.CharField('Name', max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    text = models.TextField('Text')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='review_author')
    post = models.ForeignKey('Manga', on_delete=models.CASCADE, related_name='reviews_tour')

    def __str__(self):
        return self.text


class Manga(models.Model):
    class Meta:
        verbose_name = 'Manga'
        verbose_name_plural = 'Mangas'

    TYPE_CHOICES = (
        ('e', 'Example'),
    )
    title = models.CharField('Name', max_length=255)
    description = models.TextField('Description')
    type = models.CharField('Type', choices=TYPE_CHOICES, max_length=255)
    genre = models.ManyToManyField(Genre, related_name='manga_genre', verbose_name='Genre')
    slug = models.SlugField(unique=True)
    publication_year = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(timezone.now().year),
        ]
    )
    image = models.ImageField(upload_to='manga_images/')

    def __str__(self):
        return self.title
