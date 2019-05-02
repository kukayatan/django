from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import WordForm
import operator
import csv

# Create your views here.
def words_putin(request):
        
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

                fulltext = request.POST['wform']
                wordlist = fulltext.split()
                occur = {}
                for i in wordlist:
                    if i.lower() in occur.keys():
                        occur[i] += 1
                    else:
                        occur[i] = 1
                sortedwords = sorted(occur.items(), key=operator.itemgetter(1), reverse=True)

                return render(request, 'wordcounter/results.html', {'fulltext': fulltext, 'totalamount': len(wordlist), 'sortedwords': sortedwords})
   
    else:
        form = WordForm()
        return render(request, 'wordcounter/words.html', {'form': form})


    

def export_view_gener(request):
    var = request.GET['exportgener']
    var_rep = var.replace(","," ").replace("[","").replace("]","").replace("'","").replace("(","").replace(")","")
    var_list = var_rep.split()
  
    position = 0
    x_var = ""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'
    writer = csv.writer(response)
   
    for item in var_list:
        position += 1
        if position % 2 == 0:
            writer.writerow(x_var + '  ' + item)
        else:
            x_var = item
    
    

    return response



