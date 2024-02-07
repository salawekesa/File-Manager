from django.urls import path
from .views import listing_files

urlpatterns = [
    path("",  listing_files)
]