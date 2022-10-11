from django import forms
from AppQatarWC2022.countries import Country
from AppQatarWC2022.stickers import LogoSticker

class LogoStickerRegistration(forms.Form):
    name = forms.CharField(label='Nombre',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    country = forms.ModelChoiceField(label='País',queryset=Country.objects.all(), empty_label='Seleccione País',widget=forms.Select(attrs={'class':'form-control'}))
    rarity_category = forms.ChoiceField(label='Rareza',choices=LogoSticker.Rarities.choices,widget=forms.Select(attrs={'class':'form-control'}))
    slot = forms.IntegerField(label='Slot en álbum',widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,disabled=True)
    sticker_image = forms.ImageField(label='Sticker',widget=forms.FileInput(attrs={'class':'form-control'}),required=False)

    def name(self):
        return 'Sticker de Logo'

    def class_name(self):
        return self.__class__.__name__
