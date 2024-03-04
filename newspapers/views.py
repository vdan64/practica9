from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.
class NewsDetailView(DetailView):
    model = Post
    template_name = "postdetail.html"
