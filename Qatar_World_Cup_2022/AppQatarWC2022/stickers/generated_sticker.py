from django.db import models

from .player_sticker import PlayerSticker
from .stack import StackCategory
from users.user_profile import UserProfile

class GeneratedSticker(models.Model):
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    sticker_template = models.ForeignKey(PlayerSticker,on_delete=models.CASCADE)
    stack_category = models.ForeignKey(StackCategory,on_delete=models.CASCADE)
    
    def sticker(self):
        return self.sticker_template

    def name(self):
        return self.sticker().full_name()

    def nationality(self):
        return self.sticker().nationality()

    def category(self):
        return self.stack_category.category()

    def __str__(self):
        return self.sticker()


