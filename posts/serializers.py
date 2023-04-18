from accounts.serializers import UserSerializer
from .models import Post
from rest_framework import serializers, fields

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'dated_on']