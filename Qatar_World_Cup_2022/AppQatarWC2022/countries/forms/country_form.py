from django import forms

class CountryRegistration(forms.Form):
    full_name = forms.CharField(label='Nombre',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    qualified = forms.BooleanField(label='Clasificado',widget=forms.CheckboxInput(attrs={'class':'form-control'}),initial=False)
    background_image = forms.ImageField(label='Fondo',widget=forms.FileInput(attrs={'class':'form-control'}),required=False)

    def name(self):
        return 'País'

    def class_name(self):
        return self.__class__.__name__