from django.shortcuts import render
from .forms import GenerForm
from .classgener import Generator 
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv



# Create your views here.
def gener_putin(request):
    if request.method == 'POST':
        choice = int(request.POST['wform'])
        num2 = int(request.POST['numform2'])
        if choice == 1:
            num = int(request.POST['numform'])
            res = Generator(num,num2)
            result = res.gener_number()
            return render(request, 'generator/generesult.html', {'result': result})
        elif choice == 2:
            num = int(request.POST['numform'])
            res = Generator(num,num2)
            result = res.gener_letters()
            return render(request, 'generator/generesult.html', {'result': result})
        elif choice == 3:
            num = int(request.POST['numform'])
            res = Generator(num,num2)
            result = res.gener_letters_numbers()
            return render(request, 'generator/generesult.html', {'result': result})
        else:
            num = 1
            symbol = request.POST['numform']
            res = Generator(num,num2)
            result = res.gener_custom(symbol)
            return render(request, 'generator/generesult.html', {'result': result})
        
        
    else:
        form = GenerForm()
        return render(request, 'generator/generator.html', {'form': form})  





def export_view(request):
    var = request.GET['export']
    var_rep = var.replace(","," ").replace("[","").replace("]","").replace("'","")
    var_list = var_rep.split()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'
    writer = csv.writer(response)
    for item in var_list:
        writer.writerow([item])
    
    return response










  