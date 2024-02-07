from django.shortcuts import render
from .models import IncomingFiles

# Create your views here.
def listing_files(request):
    files = IncomingFiles.objects.all()
    context = {
        "files":files
    }
    return render(request, "list_files.html", context)