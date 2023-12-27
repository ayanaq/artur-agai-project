from rest_framework import serializers
from .models import CustomUsers
from django.core.validators import RegexValidator, EmailValidator
from rest_framework.validators import UniqueValidator
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        validators=[EmailValidator(message='Enter a valid email address.')],
        required=True
    )
    username = serializers.CharField(
        validators=[
            RegexValidator(regex='^[a-zA-Z]*$', message='Only letters are allowed.'),
            UniqueValidator(queryset=CustomUsers.objects.all(), message='This username is already in use.')
        ],
        required=True
    )

    class Meta:
        model = CustomUsers
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'username': {'write_only': True},
            'email': {'write_only': True},
            'password': {'write_only': True},
        }

    def validate(self, data):
        return data

    def create(self, validated_data):
        confirmation_code = get_random_string(length=4, allowed_chars='0123456789')

        user = CustomUsers.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            is_active=False,
            confirmation_code=confirmation_code,
        )

        subject = 'Confirmation code'
        message = f'Your confirmation code is: {confirmation_code}'
        from_email = ''
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return user


class VerifyAccountSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(required=True)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = CustomUsers
        fields = ['old_password', 'new_password']

class ChangeUsernameSerializer(serializers.Serializer):
    new_username = serializers.CharField(required=True)

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class ResetPasswordSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    new_password = serializers.CharField(write_only=True, required=True)