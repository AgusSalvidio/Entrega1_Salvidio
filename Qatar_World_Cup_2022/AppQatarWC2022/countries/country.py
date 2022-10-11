from django.db import models

class Country(models.Model):
    full_name = models.CharField(max_length=50)
    background_image = models.ImageField(upload_to='backgrounds',default='background/default-background.jpg')
    qualified = models.BooleanField()

    def is_qualified(self):
        return self.qualified

    def background(self):
        return self.background_image.url

    def name(self):
        return self.full_name

    def __str__(self):
        return self.full_name 

    def class_name(self):
        return self.__class__.__name__