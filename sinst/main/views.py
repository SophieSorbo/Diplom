from django.db.models import Model
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import News, Comment, News_Like, Post
from .forms import NewsForm
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action

from .permissions import IsOwnerOrReadOnly
from .serializers import NewsSerializer, CommentSerializer, PostSerializer

from django.urls import reverse



class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterset_fields = ['user', 'date']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]



    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None, is_liked=None):
        new = self.get_object()
        user = request.user
        try:
            like = News_Like.objects.get(news=new, user=user)
            like.is_liked = not is_liked
            like.save()
            likes = News_Like.objects.filter(news=new, is_liked=True).count()
            return Response({"message": f"New '{new.title}' liked. {likes} likes"}, status=200)
        except News_Like.DoesNotExist:
            News_Like.objects.create(news=new, user=user, is_liked=True)
            return Response({"message": f"New '{new.title}' liked."}, status=200)

    @action(detail=True, methods=['POST'])
    def add_comment(self, request, pk=None):
        new = self.get_object()
        user = request.user
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(news=new, user=user)
            return Response({"message": f"New '{new.title}' commented."}, status=200)
        return Response({"error": serializer.errors}, status=400)



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ['user', 'date']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
