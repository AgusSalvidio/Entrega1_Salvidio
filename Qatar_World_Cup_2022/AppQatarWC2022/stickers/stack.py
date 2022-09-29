from django.db import models

class StackCategory(models.Model):
    category_name = models.CharField(max_length=50)

def category(self):
    return self.category_name

def __str__(self):
        return self.category()

    


    
    