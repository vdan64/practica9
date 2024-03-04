from django.shortcuts import render
from django.views.generic import UpdateView
from .models import Post
# Create your views here.
class Updatepost (UpdateView):
    model = Post
    template_name = "updatepost.html"