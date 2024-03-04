from django.contrib import admin
from django.urls import path
from .views import Updatepost, NewsDetailView

urlpatterns = [
    path('post/<int:pk>/edit/', Updatepost.as_view(),name="update_post" ),
    path("post/<int:pk>/", NewsDetailView.as_view(), name="post_detail"),
]