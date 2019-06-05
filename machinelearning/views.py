from django.shortcuts import render
from .forms import FormLR,FormSVC,nlpForm
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
        return render(request,"ml/ml_linreg.html",{'form': form})  
    
def ml_svc(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        gender = int(request.POST['gender'])
        cp = int(request.POST['cp'])
        trestbps = int(request.POST['trestbps'])
        chol = int(request.POST['chol'])
        fbs = int(request.POST['fbs'])
        restecg = int(request.POST['restecg'])
        thalach = int(request.POST['thalach'])
        exang = int(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        
        test_var = [age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak]
        myarray = np.asarray(test_var)
        
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'SVC.pkl')  
        mayarray2 = myarray.reshape(1, -1)
         
        from_joblib = joblib.load(file_path) 
        result = from_joblib.predict(mayarray2)  
        result = result.flatten().tolist()
        
        if result[0] == 0:
            result_str = "There is less than 50 % probability of the presence of heart disease in the patient."
        else:
            result_str = "There is more than 50 % probability of the presence of heart disease in the patient."

       
        
        print(result)
        form = FormSVC()
        return render(request,"ml/ml_svc.html",{'form': form,'myarray':result_str}) 

        
    else:
        form = FormSVC()
        print(form)
        return render(request,"ml/ml_svc.html",{'form': form})  

def ml_nlp(request):
    
    if request.method == 'POST':
        nlp_object = request.POST['nlpformobj']
        test_var = [nlp_object]
        
        
        module_dir = os.path.dirname(__file__)  
        file_path = os.path.join(module_dir, 'spam_detektor.pkl')  
        
         
        from_joblib = joblib.load(file_path) 
        result = from_joblib.predict(test_var) 
        result_final = result[0]
                 
        print(result)
        form = nlpForm()
        return render(request,"ml/ml_nlp.html",{'form': form,'myarray':result_final}) 

        
    else:
        form = nlpForm()
        return render(request,"ml/ml_nlp.html",{'form': form}) 