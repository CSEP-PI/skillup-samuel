from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'status', 'cpf', 'profile_img']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            cpf=validated_data['cpf'],
            profile_img=validated_data.get('profile_img', ''),
            status='A',
        )
        return user