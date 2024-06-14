from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet

router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('likes', views.LikesViewSet)
router.register('comments', views.CommentsViewSet)

urlpatterns = [
    path('', views.NewsViewSet.as_view({'get': 'list'}), name='news'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.NewsUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.NewsDeleteView.as_view(), name='delete'),
    path('like/<int:pk>/', views.LikesViewSet.as_view({'get': 'like'}), name='like'),
    path('comments/<int:pk>/', views.CommentsViewSet.as_view({'get': 'comments'}), name='comments'),
    path('?user=<int:pk>/', views.NewsViewSet.as_view({'get': 'user'}), name='user'),
] + router.urls
