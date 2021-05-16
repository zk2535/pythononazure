from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def acmestore(request):
    return render(request, "eticaret/acmestore.html")

