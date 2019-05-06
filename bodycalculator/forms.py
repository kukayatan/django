from django import forms


class FormBI(forms.Form):
    
    formweight = forms.DecimalField(max_digits=6, decimal_places=2)
    formheight = forms.DecimalField(max_digits=6, decimal_places=2)


class FormWHR(forms.Form):

    prim_choice = ((1,"Male"),(2,"Female"))
    wform = forms.ChoiceField(choices=prim_choice, label="")    
    formweist = forms.DecimalField(max_digits=6, decimal_places=2)
    formhip = forms.DecimalField(max_digits=6, decimal_places=2)