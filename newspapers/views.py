from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from .models import Post
# Create your views here.   ``
class Home(ListView):
    model = Post
    template_name = "home.html"
class NewsDetailView(DetailView):
    model = Post
    template_name = "postdetail.html"
class Updatepost (UpdateView):
    model = Post
    template_name = "updatepost.html"
    fields = ["title", "author", "body"]

