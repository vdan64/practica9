from django.contrib import admin
from django.urls import path
from .views import Updatepost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<int:pk>/edit/',Updatepost.as_view(),"update_post" ),
]


