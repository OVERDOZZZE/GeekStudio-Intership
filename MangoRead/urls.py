from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from MangoRead import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="All of project API",
      default_version='v1',
      description="Description not provided yet",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('manga/', include('manga.urls')),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
