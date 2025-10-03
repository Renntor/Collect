from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.constants import UserConstants
from users.models import User

User = get_user_model()


class PatchUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name',
            'patronymic', 'email',
        )


class UserSerializer(PatchUserSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=UserConstants.Lengths.MIN_LENGTH_PASSWORD,
        max_length=UserConstants.Lengths.MAX_LENGTH_PASSWORD
    )

    class Meta:
        fields = PatchUserSerializer.Meta.fields + (
            'password',
        )
        model = User

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
