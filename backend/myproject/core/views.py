from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
    Este viewset fornece automaticamente ações em 'list' e 'detail'.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer