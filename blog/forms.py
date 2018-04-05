from django import forms


class ttsForm(forms.Form):
    txt = forms.CharField(label="", max_length=500, widget=forms.Textarea(attrs={'class': 'form-control justify-content-start', 'style': 'height: 250px; padding-bottom: 60px; margin-botton: 0', 'id': 'txt', 'placeholder': 'Enter text here.'}))

class sentiForm(forms.Form):
    txt = forms.CharField(label="", max_length=300, widget=forms.Textarea(attrs={'class': 'form-control justify-content-start', 'style': 'height: 250px; padding-bottom: 60px; margin-botton: 0', 'id': 'txt', 'placeholder': 'Enter text here.', 'pattern': ".{25,}"}))

