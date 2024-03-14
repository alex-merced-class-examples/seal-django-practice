from django.urls import path
from first.views import hello

urlpatterns = [
    path("", hello)
]