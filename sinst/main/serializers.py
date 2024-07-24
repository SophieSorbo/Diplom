from rest_framework import serializers
from .models import News, Comment, News_Like, Users


class UsersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Users
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Like
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(read_only=True, many=True)
    likes = LikeSerializer(read_only=True, many=True)
    user = UsersSerializer(read_only=True)

    class Meta:
        model = News
        fields = '__all__'