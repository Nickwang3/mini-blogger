from django.contrib.auth.models import User
from miniblogs.models import MiniBlog, MiniBlogReply
from rest_framework import viewsets, permissions
from miniblogs.serializers import UserSerializer, MiniBlogSerializer, MiniBlogReplySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []

class MiniBlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that posts to be viewed
    """
    queryset = MiniBlog.objects.all()
    serializer_class = MiniBlogSerializer
    permission_classes = []  

class MiniBlogReplyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that posts to be viewed
    """
    queryset = MiniBlogReply.objects.all()
    serializer_class = MiniBlogReplySerializer
    permission_classes = []