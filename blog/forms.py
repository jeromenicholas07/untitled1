from django import forms

class ttsForm(forms.Form):
    txt = forms.CharField(label="inputText", max_length=500)
