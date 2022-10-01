from django.db import models

from .player_sticker import PlayerSticker
from .stack import StackCategory
from AppQatarWC2022.users.user_profile import UserProfile

class GeneratedSticker(models.Model):
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    sticker_template = models.ForeignKey(PlayerSticker,on_delete=models.CASCADE)
    sticker_category = models.CharField(max_length=50) 
    
    def slot_position(self):
        return self.sticker_template.slot_position()
    
    def sticker(self):
        return self.sticker_template

    def name(self):
        return self.sticker().full_name()

    def nationality(self):
        return self.sticker().nationality()

    def category(self):
        return self.sticker_category
    
    def rarity(self):
        return self.sticker.rarity()

    def __str__(self):
        return self.sticker()


