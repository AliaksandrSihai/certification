from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer, UserShortSerializer

# Create your views here.


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if request.user.is_staff:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            serializer = UserShortSerializer(queryset, many=True)
            return Response(serializer.data)
