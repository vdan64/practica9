from django.urls import path
from .views import NewsDetailView

urlpatterns = [
    path("post/<int:pk>/", NewsDetailView.as_view(), name="post_detail"),
]