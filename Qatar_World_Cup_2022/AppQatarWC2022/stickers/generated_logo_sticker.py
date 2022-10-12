from django.db import models

from .player_sticker import PlayerSticker
from AppQatarWC2022.users.user_profile import UserProfile
from .generated_sticker import GeneratedSticker
from .logo_sticker import LogoSticker

class GeneratedLogoSticker(GeneratedSticker):
    sticker_template = models.ForeignKey(LogoSticker,on_delete=models.CASCADE)
    
    @classmethod
    def belonging_to(cls,owner,sticker_template,sticker_category):
        return cls(
            owner = owner,
            sticker_template = sticker_template,
            sticker_category = sticker_category)

    @classmethod
    def for_empty_slot_in(cls,slot_position):
        return cls(
            owner = None,
            sticker_template = LogoSticker.for_empty_slot_in(slot_position),
            sticker_category = 'New')

    def glue_sticker(self):
        self.sticker_category = 'Glued'
        self.save()

    def update_owner_with(self,owner):
        self.owner = owner
    
    def slot_position(self):
        return self.sticker_template.slot_position()
    
    def sticker_image(self):
        return self.sticker().sticker()

    def sticker(self):
        return self.sticker_template

    def name(self):
        return self.sticker().name()

    def country(self):
        return self.sticker().nationality()

    def category(self):
        return self.sticker_category
    
    def rarity(self):
        return self.sticker.rarity()

    def __str__(self):
        return self.sticker().name()

    def class_name(self):
        return self.__class__.__name__

