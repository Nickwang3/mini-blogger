from django.contrib.auth.models import User
from miniblogs.models import MiniBlog, MiniBlogReply
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class MiniBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MiniBlog
        fields = ['id', 'author', 'text', 'created_at']

class MiniBlogReplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MiniBlogReply
        fields = ['id', 'author', 'text', 'created_at', 'replied_to']