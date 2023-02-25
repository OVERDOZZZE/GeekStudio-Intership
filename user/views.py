from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from .models import CustomUser
from .serializers import UserSerializer


class CreateUserViewSet(mixins.CreateModelMixin,
                        GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
