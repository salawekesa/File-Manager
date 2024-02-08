from django.shortcuts import render
from .models import IncomingFiles
from django.db.models import Q

# Create your views here.
def listing_files(request):
    files = IncomingFiles.objects.all()
    context = {
        "files":files
    }
    return render(request, "list_files.html", context)


def file_search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = IncomingFiles.objects.filter(
            Q(sender__icontains=query) |
            Q(recipient__icontains=query) |
            Q(subject__icontains=query) |
            Q(addressed_to__icontains=query) |
            Q(signatory__icontains=query)
        )
    return render(request, 'file_search.html', {'results': results, 'query': query})


def home(request):

    return render(request, 'home.html')


def Authpage(request):
    return render(request, "Authpage.html")
