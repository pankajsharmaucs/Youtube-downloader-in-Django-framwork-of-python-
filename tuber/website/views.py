from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def custom_404(request, exception):
    # return HttpResponse("<h1>404 page Called</h1>")
    return render(request, '404.html', status=404)
