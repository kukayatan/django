from django import forms


class FormLR(forms.Form):

    choice_gender = ((1,"Male"),(2,"Female"))
    gender = forms.ChoiceField(choices=choice_gender, label="", widget=forms.Select(attrs={'class':'form-control'}))
    choice_ethnicity = ((1,"Group A"),(2,"Group B"),(3,"Group C"),(4,"Group D"),(5,"Group E"))
    ethnicity = forms.ChoiceField(choices=choice_ethnicity, label="", widget=forms.Select(attrs={'class':'form-control'}))
    choice_parent = ((1,"High school"),(2,"Some college"),(3,"Bachelor's degree"),(4,"Master's degree"),(5,"Associate's degree"),(6,"Some high school"))
    parent = forms.ChoiceField(choices=choice_parent, label="", widget=forms.Select(attrs={'class':'form-control'}))
    lunch_gender = ((1,"Standard"),(2,"Reduced"))
    lunch = forms.ChoiceField(choices=lunch_gender, label="", widget=forms.Select(attrs={'class':'form-control'}))
    choice_preparation = ((1,"Completed"),(2,"None"))
    preparation = forms.ChoiceField(choices=choice_preparation, label="", widget=forms.Select(attrs={'class':'form-control'}))
    math = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '50', 'max': '120','id':'myRange','class':'slider'}))
    reading = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '50', 'max': '120','id':'myRange2','class':'slider'}))


class FormSVC(forms.Form):

    age = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '20', 'max': '80','id':'age_myRange','class':'slider'}))
    choice_gender = ((1,"Male"),(2,"Female"))
    gender = forms.ChoiceField(choices=choice_gender, label="", widget=forms.Select(attrs={'class':'form-control'}))
    cp = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '4','id':'cp_myRange','class':'slider'}))
    trestbps = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '70', 'max': '200','id':'trestbps_myRange','class':'slider'}))
    chol = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '85', 'max': '603','id':'chol_myRange','class':'slider'}))
    CHOICES=[(0,'fasting blood sugar < 120 mg/dl'),(1,'fasting blood sugar > 120 mg/dl')]
    fbs = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'li_ns'}))
    CHOICES2=[(0,'0'),(1,'1')]
    restecg = forms.ChoiceField(choices=CHOICES2, widget=forms.RadioSelect(attrs={'class': 'li_ns'}))
    thalach = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '70', 'max': '200','id':'thalach_myRange','class':'slider'}))
    CHOICES3=[(0,'yes'),(1,'no')]
    exang = forms.ChoiceField(choices=CHOICES3, widget=forms.RadioSelect(attrs={'class': 'li_ns'}))
    oldpeak = forms.DecimalField(max_digits=2,decimal_places=1,widget=forms.NumberInput(attrs={'type':'range', 'step': '0.1', 'min': '0', 'max': '5','id':'oldpeak_myRange','class':'slider'}))
    
class nlpForm(forms.Form):
    nlpformobj = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control'}))