from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=4)
    flag_image = models.ImageField(upload_to='flags',null=False)
        
    def flag(self):
        return self.flag_image.url

    def __str__(self):
        return self.name