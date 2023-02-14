from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=127)
    username = serializers.CharField()
    birthdate = serializers.DateField(default=None)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=is_employee, read_only=True)

    # if is_employee:
    #     print('oi')
    #     def create(self, validated_data: dict) -> User:
    #         return User.objects.create_superuser(**validated_data)    

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)