from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'manga', views.MangaViewSet)
router.register(r'review', views.ReviewViewSet)
router.register(r'genre', views.GenreViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls))
]
