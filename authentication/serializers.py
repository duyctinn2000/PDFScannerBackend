from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length = 65, min_length = 8, write_only = True)
    username = serializers.CharField(max_length = 255, min_length = 2)


    class Meta:
        model = User
        fields = ['username','password']

    def validate(self, attrs):
        username = attrs.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('Username is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 65, min_length = 8, write_only = True)
    username = serializers.CharField(max_length = 255, min_length = 2)

    class Meta:
        model = User
        fields = ['username','password']