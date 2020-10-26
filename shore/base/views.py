from rest_framework import generics

from shore.base.serializers import UserSerializer
from shore.base.models import User


class UserViewCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
