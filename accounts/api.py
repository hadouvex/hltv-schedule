from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny


from django_filters.rest_framework import DjangoFilterBackend


from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username', 'is_staff']