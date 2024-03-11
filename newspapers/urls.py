from django.contrib import admin
from django.urls import path
from .views import Updatepost, NewsDetailView, DeletePost, CreatePost 

urlpatterns = [
    path('post/<int:pk>/edit/', Updatepost.as_view(),name="update_post" ),
    path("post/<int:pk>/", NewsDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/delete/", DeletePost.as_view(), name="post_delete"),
    path("post/create/", CreatePost.as_view(), name="post_create"),
]