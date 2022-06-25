from libcst import ModuloAssign
from rest_framework.serializers import ModelSerializer
from .models import Blog, Comment, Like

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
    