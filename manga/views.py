from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from .serializers import *
from .models import *
from rest_framework import generics, viewsets, mixins, permissions
from .permissions import IsOwnerOrReadOnly
from .service import MangaFilter
from rest_framework import filters
from rest_framework.permissions import SAFE_METHODS


class MangaPagination(PageNumberPagination):
    page_size = 12
    page_query_param = 'page_size'
    max_page_size = 100


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = MangaFilter
    pagination_class = MangaPagination
    search_fields = ['title']
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    permission_classes = [permissions.IsAdminUser]


