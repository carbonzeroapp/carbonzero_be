from allauth.account.utils import setup_user_email
from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from users.models import User


@extend_schema_serializer(
    exclude_fields=('email',),
)
class CustomLoginSerializer(LoginSerializer):
    pass


class CustomRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    date_of_birth = serializers.DateField()
    gender = serializers.IntegerField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def save(self, request):
        validated_data = self.validated_data

        user = User.objects.create_user(
            username=validated_data['username'], email=validated_data['email'],
            date_of_birth=validated_data['date_of_birth'], gender=validated_data['gender'],
            password=validated_data['password'], password2=validated_data['password2']
        )
        setup_user_email(request, user, [])

        return user


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = User
        fields = UserDetailsSerializer.Meta.fields + ('date_of_birth', 'gender', 'joined')
        read_only_fields = ('email',)
