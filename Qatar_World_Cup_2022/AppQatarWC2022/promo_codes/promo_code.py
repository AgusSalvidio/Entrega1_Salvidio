from django.db import models


class PromoCode(models.Model):
   code = models.CharField(max_length=15)

   @classmethod
   def composed_of(cls, code):
      return cls(code = code)

   @classmethod
   def from_form(cls, form_data):
      return cls.composed_of(code=form_data.get('code'))
   
   def __str__(self):
        return self.code

   def synchronize_with(self,updated_promo_code):
      self.code = updated_promo_code.code

   def class_name(self):
        return self.__class__.__name__
