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

    