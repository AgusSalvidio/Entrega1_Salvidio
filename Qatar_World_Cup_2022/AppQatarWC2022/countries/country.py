from django.db import models

class Country(models.Model):
    full_name = models.CharField(max_length=50)
    background_image = models.ImageField(upload_to='backgrounds',default='background/default-background.jpg')
    qualified = models.BooleanField()

    @classmethod
    def composed_of(cls, full_name,qualified,background_image):
      return cls(
        full_name = full_name,
        qualified = qualified,
        background_image = background_image)
    
    @classmethod
    def from_form(cls, form_data):
      return cls.composed_of(
        full_name=form_data.get('full_name'),
        qualified =form_data.get('qualified'),
        background_image = form_data.get('background_image'))

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