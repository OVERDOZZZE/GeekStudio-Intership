from rest_framework.validators import UniqueValidator
from .models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False)
    nickname = serializers.CharField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'image', 'nickname']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        if image:
            user.image = image
        user.save()
        return user


