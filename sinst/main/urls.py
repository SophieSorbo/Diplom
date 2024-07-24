from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet

router = DefaultRouter()
router.register('news', NewsViewSet)

urlpatterns = [
    path('', views.NewsViewSet.as_view({'get': 'list'}), name='news'),
    path('create/', views.NewsViewSet.as_view({'post': 'create'}), name='news_create'),
    path('update/<int:pk>/', views.NewsViewSet.as_view({'put': 'update'}), name='news_update'),
    path('delete/<int:pk>/', views.NewsViewSet.as_view({'delete': 'destroy'}), name='news_delete'),
    path('<int:pk>/', views.NewsViewSet.as_view({'get': 'retrieve'}), name='news_detail'),
    path('?user=<int:pk>/', views.NewsViewSet.as_view({'get': 'user'}), name='user'),
    path('like/<int:pk>/', views.NewsViewSet.as_view({'post': 'like'}), name='like'),
    path('comment/<int:pk>/', views.NewsViewSet.as_view({'post': 'comment'}), name='comment'),
] + router.urls
