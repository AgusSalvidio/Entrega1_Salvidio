from email.policy import default
from django.db import models

import datetime
from django.contrib.auth.models import User 

current_date = datetime.datetime.today()

class UserProfile(models.Model):
    internal_user = models.ForeignKey(User,on_delete=models.CASCADE)
    birthdate = models.DateField()
    country = models.CharField(max_length=50)     # In the next stage of the project this should become a singleSelectionList, for now will be only a string
    avatar_image = models.ImageField(upload_to='avatars', default='avatars/default_avatar.jpg',null=False)
    
    def age(self):
        return current_date.year - self.birthdate.year

    def full_name(self):
        return f'{self.internal_user.first_name} {self.internal_user.last_name}'
    
    def avatar(self):
        return self.avatar_image.url

    def __str__(self):
        return self.full_name()

