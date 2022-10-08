from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    background_image = models.ImageField(upload_to='backgrounds',null=False)
    qualified = models.BooleanField()

    def is_qualified(self):
        return self.qualified

    def background(self):
        return self.background_image.url

    def __str__(self):
        return self.name