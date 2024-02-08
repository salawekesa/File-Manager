from django.shortcuts import render

# Create your views here.

def Authpage(request):
    return render(request, "Authpage.html")