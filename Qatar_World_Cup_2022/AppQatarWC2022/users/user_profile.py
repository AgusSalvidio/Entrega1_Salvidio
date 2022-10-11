from django.db import models

import datetime
from django.contrib.auth.models import User 
from AppQatarWC2022.countries import Country

current_date = datetime.datetime.today()

class UserProfile(models.Model):
    internal_user = models.OneToOneField(User,on_delete=models.CASCADE)
    birthdate = models.DateField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    avatar_image = models.ImageField(upload_to='avatars', default='avatars/default-avatar.jpg')
    
    @classmethod
    def composed_of(cls, internal_user,birthdate, country, avatar_image):
      return cls(
        internal_user = internal_user,
        birthdate = birthdate,
        country = country,
        avatar_image = avatar_image)

    @classmethod
    def from_form_using(cls,form_data,user):
        return cls.composed_of(
                internal_user = user,
                birthdate = form_data.get('birthdate'),
                country = form_data.get('country'),
                avatar_image = form_data.get('avatar_image'))

    def last_login(self):
        return self.internal_user.last_login
   
    def age(self):
        return current_date.year - self.birthdate.year

    def first_name(self):
        return self.internal_user.first_name
    
    def last_name(self):
        return self.internal_user.last_name

    def email(self):
        return self.internal_user.email

    def username(self):
        return self.internal_user.get_username()

    def birth_date(self):
        return self.birthdate

    def full_name(self):
        return f'{self.internal_user.first_name} {self.internal_user.last_name}'
    
    def avatar(self):
        return self.avatar_image.url

    def nationality(self):
        return self.country

    def synchronize_with(self,updated_user_profile):
        self.internal_user = updated_user_profile.internal_user
        self.birthdate = updated_user_profile.birthdate
        self.country = updated_user_profile.country
        if updated_user_profile.avatar_image != None:
            self.avatar_image = updated_user_profile.avatar_image
     
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.full_name()

