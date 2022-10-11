from django.db import models

from AppQatarWC2022.countries import Country
from .sticker import Sticker

class PlayerPosition(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class PlayerSticker(Sticker):
    birthdate = models.DateField()
    position =  models.ForeignKey(PlayerPosition,on_delete=models.CASCADE)  

    @classmethod
    def for_empty_slot_in(cls,slot_position):
        return cls(
            full_name = None,
            country = None,
            birthdate = None,
            position =  None, 
            sticker_image = None,
            slot = slot_position,
            rarity_category = None)

    @classmethod
    def composed_of(cls, full_name,country, birthdate, position, sticker_image, slot, rarity_category):
      return cls(
        full_name = full_name,
        country = country,
        birthdate = birthdate,
        position = position,
        sticker_image = sticker_image,
        slot = slot,
        rarity_category = rarity_category)

    @classmethod
    def from_form(cls, form_data):
      return cls.composed_of(
        full_name = form_data.get("full_name"),
        country = form_data.get("country"),
        birthdate = form_data.get("birthdate"),
        position = form_data.get("position"),
        sticker_image = form_data.get("sticker_image"),
        rarity_category = form_data.get("rarity_category"),
        slot = form_data.get("slot"))
    
    def name(self):
        return self.full_name
    
    def __str__(self):
        return self.name()

    def synchronize_with(self,updated_player_sticker):
        self.full_name = updated_player_sticker.full_name
        self.country =   updated_player_sticker.country 
        self.birthdate = updated_player_sticker.birthdate
        self.position =   updated_player_sticker.position
        self.sticker_image = updated_player_sticker.sticker_image
        self.slot = updated_player_sticker.slot
        self.rarity_category = updated_player_sticker.rarity_category
     
    def class_name(self):
        return self.__class__.__name__



