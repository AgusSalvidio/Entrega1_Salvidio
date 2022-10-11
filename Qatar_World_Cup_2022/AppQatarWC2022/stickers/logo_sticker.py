from django.db import models

from .sticker import Sticker

class LogoSticker(Sticker):
     
    @classmethod
    def for_empty_slot_in(cls,slot_position):
        return cls(
            name = None,
            country = None, 
            sticker_image = None,
            slot = slot_position,
            rarity_category = None)

    @classmethod
    def composed_of(cls, name, country, sticker_image, slot, rarity_category):
      return cls(
        name = name,
        country = country,
        sticker_image = sticker_image,
        slot = slot,
        rarity_category = rarity_category)

    @classmethod
    def from_form(cls, form_data):
      return cls.composed_of(
        name = form_data.get("name"),
        last_name = form_data.get("last_name"),
        country = form_data.get("country"),
        sticker_image = form_data.get("sticker_image"),
        rarity_category = form_data.get("rarity_category"),
        slot = form_data.get("slot"))

    def __str__(self):
        return self.full_name()

    def synchronize_with(self,updated_logo_sticker):
        self.name = updated_logo_sticker.name
        self.country =  updated_logo_sticker.country 
        self.sticker_image = updated_logo_sticker.sticker_image
        self.slot = updated_logo_sticker.slot
        self.rarity_category = updated_logo_sticker.rarity_category
     
    def class_name(self):
        return self.__class__.__name__



