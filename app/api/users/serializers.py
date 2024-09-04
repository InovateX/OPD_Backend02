from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  # Hide password in GET responses
        }

    def create(self, validated_data):
        user = UserModel.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            phone_no=validated_data['phone_no'],
            password=validated_data['password'],
            identification_type=validated_data['identification_type'],
            id_no=validated_data['id_no'],
            age=validated_data['age'],
            location=validated_data['location'],
            state=validated_data['state'],
            city=validated_data['city'],
            pin_code=validated_data['pin_code'],
        )
        user.set_password(validated_data['password'])  # Encrypt password
        user.save()
        return user
