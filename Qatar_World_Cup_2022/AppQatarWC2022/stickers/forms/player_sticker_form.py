from django import forms
from AppQatarWC2022.countries import Country
from AppQatarWC2022.stickers import PlayerPosition,PlayerSticker

class PlayerStickerRegistration(forms.Form):
    name = forms.CharField(label='Nombre Completo',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    birthdate = forms.DateField(label='Fecha de Nacimiento',widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    country = forms.ModelChoiceField(label='País',queryset=Country.objects.all(), empty_label='Seleccione País',widget=forms.Select(attrs={'class':'form-control'}))
    position =forms.ModelChoiceField(label='Posición',queryset=PlayerPosition.objects.all(), empty_label='Seleccione Posición',widget=forms.Select(attrs={'class':'form-control'}))
    rarity_category = forms.ChoiceField(label='Rareza',choices=PlayerSticker.Rarities.choices,widget=forms.Select(attrs={'class':'form-control'}))
    slot = forms.IntegerField(label='Slot en álbum',widget=forms.NumberInput(attrs={'class':'form-control'}))
    sticker_image = forms.ImageField(label='Sticker',widget=forms.FileInput(attrs={'class':'form-control'}),required=False)

    def name(self):
        return 'Sticker de Jugador'

    def class_name(self):
        return self.__class__.__name__
