from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=250)
    body = models.CharField(max_length=300)
    date = models.DateField()
    author = models.CharField(max_length=50)
    image_template = models.ImageField(upload_to='assets')

    def image(self):
        return self.image_template.url

    def __str__(self):
        return self.title