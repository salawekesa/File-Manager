from django.urls import path
from . import views
from .views import Authpage


urlpatterns = [
    path("", views.home, name="home"),
    path("list",  views.listing_files, name="listfiles"),
    path("files", views.file_search, name="filesearch"),
]