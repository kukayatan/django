from django.shortcuts import render

# Create your views here.
def ml_view(request):
    
    return render(request,"ml/ml_home.html",{})