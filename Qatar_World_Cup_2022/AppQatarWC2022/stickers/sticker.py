from django.db import models

from AppQatarWC2022.countries import Country

class Sticker(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)    
    sticker_image = models.ImageField(upload_to='stickers', default='stickers/default-sticker.jpg')
    slot = models.IntegerField()
    Rarities = models.TextChoices('Rareza', 'Común Épica Legendaria')
    rarity_category = models.CharField(max_length=50,choices=Rarities.choices) 

    def full_name(self):
        return self.name

    def slot_position(self):
        return self.slot
    
    def nationality(self):
        return self.country
    
    def rarity(self):
        return self.rarity_category

    def sticker(self):
        return self.sticker_image.url



