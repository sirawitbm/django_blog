from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView, name='blog-home'),
    path('create/', views.PostCreateView, name='blog-create'),
    path('post/<int:pk>', views.PostDetailView, name='blog-detail'),
    path('about/', views.about, name='blog-about'),
]
