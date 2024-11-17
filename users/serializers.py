from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'email', 'phone_number', 'address')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        # after creating user, set password
        user.set_password(validated_data['password'])
        user.save()
        return user