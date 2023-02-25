from django_filters import rest_framework as filters
from .models import Manga, Genre


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MangaFilter(filters.FilterSet):
    genre = CharFilterInFilter(field_name='genre__slug', lookup_expr='in')
    publication_year = filters.RangeFilter(field_name='publication_year', lookup_expr='in')

    class Meta:
        model = Manga
        fields = 'title publication_year'.split()
