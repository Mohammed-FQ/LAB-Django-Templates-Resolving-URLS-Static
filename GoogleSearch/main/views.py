from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest




def home_view(request: HttpRequest):
    return render(request, 'main/home.html')

def terms_view(request):
    return render(request, 'main/terms.html')

def mode_view(request:HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
    return response

