from django.contrib.auth.models import User, Group
from miniblogs.models import MiniBlog
from rest_framework import viewsets, permissions
from miniblogs.serializers import UserSerializer, GroupSerializer, MiniBlogSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class MiniBlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that posts to be viewed
    """
    queryset = MiniBlog.objects.all()
    serializer_class = MiniBlogSerializer
    permission_classes = []  
