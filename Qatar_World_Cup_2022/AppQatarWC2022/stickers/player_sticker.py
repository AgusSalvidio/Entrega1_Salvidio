from django.db import models

from AppQatarWC2022.countries import Country

class PlayerSticker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)    
    birthdate = models.DateField()
    position =  models.CharField(max_length=50)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def nationality(self):
        return self.country.name

    def __str__(self):
        return self.full_name()
