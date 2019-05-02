from django.shortcuts import render

# Create your views here.

def home_view(request):
    
    return render(request,"portfolio/home.html",{})


def about(request):
    
    return render(request,"portfolio/about.html",{})
