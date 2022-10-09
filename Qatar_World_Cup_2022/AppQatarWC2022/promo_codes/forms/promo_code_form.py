from django import forms

class PromoCodeRegistration(forms.Form):
    
    code = forms.CharField(label='Código',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

    def name(self):
        return 'Código Promocional'

    def class_name(self):
        return self.__class__.__name__