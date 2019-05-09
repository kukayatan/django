from django import forms

class WordForm(forms.Form):
    wform = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control'}))