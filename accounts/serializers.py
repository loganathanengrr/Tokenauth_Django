from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'confirm_password',
            'is_staff',
            'is_superuser',
        )
    
    def create(self, validated_data):
        user = self.instance
        is_staff = validated_data.get('is_staff');
        is_superuser = validated_data.get('is_superuser')
        validated_data.pop('confirm_password')

        if is_staff and is_superuser:
            user = User.objects.create_superuser(**validated_data)
        elif is_staff:
            user = User.objects.create_staffuser(**validated_data)
        else:
           user = User.objects.create_user(**validated_data)

        return user

    def validate(self, attrs):
        attrs = super(UserSerializer, self).validate(attrs)
        password = attrs.get('password')
        password_2 = attrs.get('confirm_password')

        if password == password_2:
            try:
                validate_password(password, self.instance)
            except ValidationError as e:
                raise serializers.ValidationError(list(e.messages))
        else: 
            raise serializers.ValidationError("Password mismatch, Please enter correct passwords")
        return attrs
