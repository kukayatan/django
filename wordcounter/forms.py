from django import forms

class WordForm(forms.Form):
    wform = forms.CharField(label='',widget=forms.Textarea(attrs={"rows":15,"cols":70}))