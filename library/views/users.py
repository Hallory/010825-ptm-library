from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView

from library.permissions import IsAdminOnly
from library.serializers.user import UserRetrieveSerializer, UserSerializer

User = get_user_model()


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOnly]


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer
    permission_classes = [IsAdminOnly]
