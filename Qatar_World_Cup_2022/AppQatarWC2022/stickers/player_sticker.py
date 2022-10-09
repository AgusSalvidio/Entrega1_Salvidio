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
    Rarities = models.TextChoices('Rareza', 'Común Épica Legendaria')
    rarity_category = models.CharField(max_length=50,choices=Rarities.choices) 

    @classmethod
    def for_empty_slot_in(cls,slot_position):
        return cls(
            first_name = None,
            last_name = None,
            country = None,
            birthdate = None,
            position =  None, 
            sticker_image = None,
            slot = slot_position,
            rarity_category = None)

    @classmethod
    def composed_of(cls, first_name,last_name, country, birthdate, position, sticker_image, slot, rarity_category):
      return cls(
        first_name = first_name,
        last_name = last_name,
        country = country,
        birthdate = birthdate,
        position = position,
        sticker_image = sticker_image,
        slot = slot,
        rarity_category = rarity_category)

    @classmethod
    def from_form(cls, form_data):
      return cls.composed_of(
        first_name = form_data.get("first_name"),
        last_name = form_data.get("last_name"),
        country = form_data.get("country"),
        birthdate = form_data.get("birthdate"),
        position = form_data.get("position"),
        sticker_image = form_data.get("sticker_image"),
        rarity_category = form_data.get("rarity_category"),
        slot = form_data.get("slot"))

    def slot_position(self):
        return self.slot
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def nationality(self):
        return self.country
    
    def rarity(self):
        return self.rarity_category

    def sticker(self):
        return self.sticker_image.url

    def __str__(self):
        return self.full_name()

    def synchronize_with(self,updated_player_sticker):
        self.first_name = updated_player_sticker.first_name
        self.last_name = updated_player_sticker.last_name
        self.country =   updated_player_sticker.country 
        self.birthdate = updated_player_sticker.birthdate
        self.position =   updated_player_sticker.position
        self.sticker_image = updated_player_sticker.sticker_image
        self.slot = updated_player_sticker.slot
        self.rarity_category = updated_player_sticker.rarity_category
     
    def class_name(self):
        return self.__class__.__name__



