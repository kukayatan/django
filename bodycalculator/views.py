from django.shortcuts import render
from .forms import FormBI,FormWHR
from .classbodycalc import Calculation 

def bodycalc_view(request):
    
    return render(request,"bodycalc/body_init.html",{})

def bmi(request):
    
    if request.method == 'POST':
        weight = int(request.POST['formweight'])
        height = int(request.POST['formheight'])
        calc = Calculation()
        calc_bmi = calc.bmi(weight,height)
        return render(request, 'bodycalc/bmi_result.html', {'result': calc_bmi})
        
    else:
        form = FormBI()
        return render(request, 'bodycalc/bmi.html', {'form': form})  

def whr(request):
    
    if request.method == 'POST':
        gender = request.POST['wform']
        weist = int(request.POST['formweist'])
        hip = int(request.POST['formhip'])
        whr_obj = Calculation()
        whr_result = whr_obj.whr(weist, hip, gender)
        return render(request, 'bodycalc/whr_result.html', {'result': whr_result})
    else:
        form = FormWHR()
        return render(request, 'bodycalc/whr.html', {'form': form})  

        

        
   