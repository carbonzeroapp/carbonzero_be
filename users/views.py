from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from users.serializers import CustomUserDetailsSerializer

UserModel = get_user_model()


class UserView(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = UserModel.objects.all()
    serializer_class = CustomUserDetailsSerializer
