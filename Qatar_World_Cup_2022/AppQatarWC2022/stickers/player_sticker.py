from django.db import models

class PlayerSticker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)     # In the next stage of the project this should become a singleSelectionList, for now will be only a string
    birthdate = models.DateField()
    position =  models.CharField(max_length=50)     # In the next stage of the project this should become a singleSelectionList, for now will be only a string

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()
