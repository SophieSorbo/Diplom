from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, PostViewSet

router = DefaultRouter()
router.register('news', NewsViewSet)

urlpatterns = [
    path('', views.NewsViewSet.as_view({'get': 'list'}), name='news'),
    path('?user=<int:pk>/', views.NewsViewSet.as_view({'get': 'user'}), name='user'),
    path('like/<int:pk>/', views.NewsViewSet.as_view({'post': 'like'}), name='like'),
    path('likes/<int:pk>/', views.NewsViewSet.as_view({'get': 'likes'}), name='likes'),
    path('comment/<int:pk>/', views.NewsViewSet.as_view({'post': 'comment'}), name='comment'),
    path('post/', views.PostViewSet.as_view({'get': 'list'}), name='post'),
    path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'post'}), name='post'),
] + router.urls
