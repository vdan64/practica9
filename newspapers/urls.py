from django.contrib import admin
from django.urls import path
from .views import Updatepost

urlpatterns = [
    path('post/<int:pk>/edit/',Updatepost.as_view(),"update_post" ),
]


