from django.db.models import Model
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated

from .models import News, Comments, Likes
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet, ViewSet

from .permissions import IsOwnerOrReadOnly
from .serializers import NewsSerializer, LikesSerializer, CommentsSerializer




class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterset_fields = ['user', 'date']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def news(request):
        news = News.objects.order_by('-date')[:8]
        data = {'news': news, 'title': 'SInst'}
        return render(request, 'main/index.html', data)


class NewsDetailView(DetailView):
    model = News
    template_name = 'main/detail.html'
    context_object_name = 'news'

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'main/update.html'
    form_class = NewsForm

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'main/delete.html'
    success_url = '/'

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'
    form = NewsForm
    data = {'form': form, 'error': error}
    return render(request, 'main/create.html', data)


class LikesViewSet(ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def like(self, request, pk):
        like = self.get_object()
        return render(request, 'main/like.html', {'like': like})


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def comments(self, request, pk):
        comments = self.get_object()
        return render(request, 'main/comments.html', {'comments': comments})

