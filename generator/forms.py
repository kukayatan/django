from django import forms


class GenerForm(forms.Form):
    prim_choice = (("",""),(1,"generate passwords cotaining just numbers"),(2,"generate passwords cotaining just letters"),(3,"generate passwords cotaining numbers and letters"),(4,"generate passwords cotaining customized amount of symbols"))
    wform = forms.ChoiceField(choices=prim_choice, label="")
    numform = forms.CharField(max_length=50,min_length=1,label="")
    numform2 = forms.IntegerField(max_value=1000,min_value=1,label="")

