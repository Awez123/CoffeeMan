from django.shortcuts import render

# Create your views here.

def greenCoffe(request):
    return render(request,"greencoffe.html")

def decord(request):
    return render(request,"decord.html")

def caffeMac(request):
    return render(request,"caffemac.html")

def americano(request):
    return render(request,"americano.html")

def coldCoffe(request):
    return render(request,"coldCoffe.html")

def index(request): 
    return render(request,'intro.html')
