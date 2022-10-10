from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from AppQatarWC2022.countries import Country

class UserRegistration(UserCreationForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label='Seleccione País',widget=forms.Select(attrs={'class':'form-control'}))
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Repita la contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    avatar = forms.ImageField(label='Avatar',widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username','password1','password2']
        help_texts = {k:"" for k in fields}

    def name(self):
        return 'Registro de Perfil de Usuario'

    def class_name(self):
        return self.__class__.__name__

class UserProfileUpdate(forms.Form):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label='Seleccione País',widget=forms.Select(attrs={'class':'form-control'}))
    avatar = forms.ImageField(label='Avatar',widget=forms.FileInput(attrs={'class':'form-control'}),required=False)

    def name(self):
        return 'Actualización de Perfil de Usuario'

    def class_name(self):
        return self.__class__.__name__

