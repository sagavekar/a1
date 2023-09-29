from django.http import HttpResponse
from django.shortcuts import render # to render html page

def Home(request):
    return render(request,"index.html") # rendering HTML page

def contact(request):
    return render(request,"contact.html") # rendering HTML page

