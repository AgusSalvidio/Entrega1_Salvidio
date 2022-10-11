from django.db import models

from AppQatarWC2022.users.user_profile import UserProfile

class GeneratedSticker(models.Model):
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Categories = models.TextChoices('Categories', 'New Glued Swapped')
    sticker_category = models.CharField(max_length=50,choices=Categories.choices) 
    
    def __str__(self):
        return 'Sticker Generado'

    def class_name(self):
        return self.__class__.__name__

