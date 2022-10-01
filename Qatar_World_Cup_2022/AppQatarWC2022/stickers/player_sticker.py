from django.db import models

from AppQatarWC2022.countries import Country

class PlayerPosition(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=4)

    def __str__(self):
        return self.name

class PlayerSticker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)    
    birthdate = models.DateField()
    position =  models.ForeignKey(PlayerPosition,on_delete=models.CASCADE)  
    sticker_image = models.ImageField(upload_to='stickers', default='stickers/default_sticker.jpg',null=False)
    slot = models.IntegerField()
    rarity_category = models.CharField(max_length=50) 

    def slot_position(self):
        return self.slot
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def nationality(self):
        return self.country.name
    
    def rarity(self):
        return self.rarity_category

    def sticker(self):
        return self.sticker_image.url

    def __str__(self):
        return self.full_name()




