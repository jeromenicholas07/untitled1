from django import forms


class ttsForm(forms.Form):
    txt = forms.CharField(label="Enter text", max_length=500, widget=forms.TextInput(attrs={'class': 'form-control col', 'style': 'height: 100px', 'id': 'txt'}))

