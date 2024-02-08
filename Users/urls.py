from django.urls import path
from . import views
from .views import Authpage

urlpatterns = [
    path("", Authpage),
]