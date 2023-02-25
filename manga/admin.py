from django.contrib import admin
from .models import Genre, Manga, Review


admin.site.register(Manga)
admin.site.register(Genre)
admin.site.register(Review)
