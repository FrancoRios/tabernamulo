from django.shortcuts import render

# Create your views here.
def homex(request):
    return render(request, 'home/index.html', {})

def recetax(request):
    return render(request, 'home/PAGES/recetas.html', {})

def barex(request):
    return render(request, 'home/PAGES/bares.html', {})

def logix(request):
    return render(request, 'home/PAGES/login.html', {})