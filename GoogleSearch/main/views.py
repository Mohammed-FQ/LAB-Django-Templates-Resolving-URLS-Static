from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home_view(request: HttpRequest):
    return render(request, 'main/home.html')

def terms_view(request: HttpRequest):
    return render(request, 'main/terms.html')
def test_view(request: HttpRequest):
    return render(request, 'main/base.html')