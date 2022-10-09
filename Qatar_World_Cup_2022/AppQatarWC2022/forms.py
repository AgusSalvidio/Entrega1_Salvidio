from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from AppQatarWC2022.countries import Country
from AppQatarWC2022.stickers import PlayerPosition,PlayerSticker

class SignIn(AuthenticationForm):
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
    password= forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class PromoCodeRegistration(forms.Form):
    
    code = forms.CharField(label='Código',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

    def name(self):
        return 'Código Promocional'

    def class_name(self):
        return self.__class__.__name__


class PlayerStickerRegistration(forms.Form):
    first_name = forms.CharField(label='Nombre',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Apellido',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    birthdate = forms.DateField(label='Fecha de Nacimiento',widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    country = forms.ModelChoiceField(label='País',queryset=Country.objects.all(), empty_label=None,widget=forms.Select(attrs={'class':'form-control'}))
    position =forms.ModelChoiceField(label='Posición',queryset=PlayerPosition.objects.all(), empty_label=None,widget=forms.Select(attrs={'class':'form-control'}))
    rarity_category = forms.ChoiceField(label='Rareza',choices=PlayerSticker.Rarities.choices,widget=forms.Select(attrs={'class':'form-control'}))
    slot = forms.IntegerField(label='Slot en álbum',widget=forms.NumberInput(attrs={'class':'form-control'}))
    sticker_image = forms.ImageField(label='Sticker',widget=forms.FileInput(attrs={'class':'form-control'}))

    def name(self):
        return 'Sticker de Jugador'

    def class_name(self):
        return self.__class__.__name__

class UserRegistration(UserCreationForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label=None,widget=forms.Select(attrs={'class':'form-control'}))
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Repita la contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    avatar = forms.ImageField(label='Avatar',widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username','password1','password2']
        help_texts = {k:"" for k in fields}

class CountryRegistration(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    short_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    avatar = forms.ImageField(label='Bandera',widget=forms.FileInput(attrs={'class':'form-control'}))