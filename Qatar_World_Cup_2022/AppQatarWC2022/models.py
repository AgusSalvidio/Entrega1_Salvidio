from django.db import models
import datetime

current_date = datetime.datetime.today()

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    country = models.CharField(max_length=50)     # In the next stage of the project this should become a singleSelectionList, for now will be only a string
    email = models.EmailField()

    def age(self):
        return current_date.year - self.birthdate.year

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

class PlayerCard(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)     # In the next stage of the project this should become a singleSelectionList, for now will be only a string
    birthdate = models.DateField()
    position =  models.CharField(max_length=50)     # In the next stage of the project this should become a singleSelectionList, for now will be only a string

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

class PromoCode(models.Model):
   code = models.CharField(max_length=15)
   
   def __str__(self):
        return self.code
