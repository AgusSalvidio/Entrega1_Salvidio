from django.db import models

from .player_sticker import PlayerSticker
from AppQatarWC2022.users.user_profile import UserProfile

class GeneratedSticker(models.Model):
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    sticker_template = models.ForeignKey(PlayerSticker,on_delete=models.CASCADE)
    Categories = models.TextChoices('Categories', 'New Glued Swapped')
    sticker_category = models.CharField(max_length=50,choices=Categories.choices) 
    
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
            sticker_template = PlayerSticker.for_empty_slot_in(slot_position),
            sticker_category = 'New')

    def glue_sticker(self):
        self.sticker_category = 'Glued'

    def update_owner_with(self,owner):
        self.owner = owner
    
    def slot_position(self):
        return self.sticker_template.slot_position()
    
    def sticker_image(self):
        return self.sticker().sticker()

    def sticker(self):
        return self.sticker_template

    def name(self):
        return self.sticker().full_name()

    def country(self):
        return self.sticker().nationality()

    def category(self):
        return self.sticker_category
    
    def rarity(self):
        return self.sticker.rarity()

    def __str__(self):
        return self.sticker().full_name()

    def class_name(self):
        return self.__class__.__name__

