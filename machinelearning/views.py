from django.shortcuts import render
from .forms import FormLR
import numpy as np
import os
from sklearn.externals import joblib    
      
        
        


# Create your views here.
def ml_view(request):
    
    return render(request,"ml/ml_home.html",{})


def ml_linreg(request):
    if request.method == 'POST':
        wgender = request.POST['gender']
        wlunch = request.POST['lunch']
        wethnicity = request.POST['ethnicity']
        wprep = request.POST['preparation']
        wparent = request.POST['parent']
        wmath = int(request.POST['math'])
        wmath_list = [wmath] 
        wreading = int(request.POST['reading'])
        wreading_list = [wreading]
        
        if wgender == 1:
            wgender_list = [0,1]
        else:
            wgender_list = [1,0]

        if wlunch == 1:
            wlunch_list = [0,1]
        else:
            wlunch_list = [1,0]

        if wethnicity == 1:
            wethnicity_list = [1,0,0,0,0]
        elif wethnicity == 2:
            wethnicity_list = [0,1,0,0,0]
        elif wethnicity == 3:
            wethnicity_list = [0,0,1,0,0]
        elif wethnicity == 4:
            wethnicity_list = [0,0,0,1,0]
        else:
            wethnicity_list = [0,0,0,0,1]

        if wprep == 1:
            wprep_list = [1,0]
        else:
            wprep_list = [0,1]

        if wparent == 1:
            wparent_list = [0,0,1,0,0,0]
        elif wparent == 2:
            wparent_list = [0,0,0,0,1,0]
        elif wparent == 3:
            wparent_list = [0,1,0,0,0,0]
        elif wparent == 4:
            wparent_list = [0,0,0,1,0,0]
        elif wparent == 5:
            wparent_list = [1,0,0,0,0,0]
        else:
           wparent_list = [0,0,0,0,0,1]

        all_list = wmath_list + wreading_list + wlunch_list + wgender_list + wethnicity_list + wparent_list + wprep_list
        myarray = np.asarray(all_list)
        
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'regres_model.pkl')  
        mayarray2 = myarray.reshape(1, -1)
         
        from_joblib = joblib.load(file_path) 
        result = from_joblib.predict(mayarray2) 
        result = result.flatten().round(1).tolist()
              
        form = FormLR()
        return render(request,"ml/ml_linreg.html",{'form': form,'myarray':result[0]})  

        
        

        
    else:
        form = FormLR()
        print(form)
        return render(request,"ml/ml_linreg.html",{'form': form})  
    
