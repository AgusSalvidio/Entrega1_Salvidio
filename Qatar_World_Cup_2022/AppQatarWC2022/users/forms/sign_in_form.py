from django import forms
from django.contrib.auth.forms import AuthenticationForm

class SignIn(AuthenticationForm):
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
    password= forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def name(self):
        return 'Logueo'

    def class_name(self):
        return self.__class__.__name__
