from django.urls import path
from .views import listing_files, file_search

urlpatterns = [
    path("",  listing_files),
    path("files/", file_search)
]