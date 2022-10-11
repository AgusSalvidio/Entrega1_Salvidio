from django import forms

class MessageRegistration(forms.Form):
    content = forms.CharField(label_suffix='', label='Message', widget=forms.Textarea(attrs={'class':'form-control'}))
