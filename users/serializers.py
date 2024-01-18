from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериалайзер для модели пользователя"""

    class Meta:
        model = User
        fields = ("email", "password")


class UserShortSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "email",
        )
