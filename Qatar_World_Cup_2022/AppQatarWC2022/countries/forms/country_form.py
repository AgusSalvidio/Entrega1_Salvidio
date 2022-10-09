from django import forms

class CountryRegistration(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    short_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    avatar = forms.ImageField(label='Bandera',widget=forms.FileInput(attrs={'class':'form-control'}))