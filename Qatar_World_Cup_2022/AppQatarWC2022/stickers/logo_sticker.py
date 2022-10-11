from django.db import models

from .sticker import Sticker

class LogoSticker(Sticker):
     
    @classmethod
    def for_empty_slot_in(cls,slot_position):
        return cls(
            full_name = None,
            country = None, 
            sticker_image = None,
            slot = slot_position,
            rarity_category = None)

    @classmethod
    def composed_of(cls, full_name, country, sticker_image, slot, rarity_category):
      return cls(
        full_name = full_name,
        country = country,
        sticker_image = sticker_image,
        slot = slot,
        rarity_category = rarity_category)

    @classmethod
    def from_form(cls, form_data):
      return cls.composed_of(
        full_name = form_data.get("full_name"),
        country = form_data.get("country"),
        sticker_image = form_data.get("sticker_image"),
        rarity_category = form_data.get("rarity_category"),
        slot = form_data.get("slot"))

    def name(self):
        return self.full_name

    def __str__(self):
        return self.name()

    def synchronize_with(self,updated_logo_sticker):
        self.full_name = updated_logo_sticker.full_name
        self.country =  updated_logo_sticker.country 
        self.sticker_image = updated_logo_sticker.sticker_image
        self.slot = updated_logo_sticker.slot
        self.rarity_category = updated_logo_sticker.rarity_category
     
    def class_name(self):
        return self.__class__.__name__



