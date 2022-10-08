from django.db import models
from assertions import enforce_not_blank

class PromoCode(models.Model):
   code = models.CharField(max_length=15)

   @classmethod
   def composed_of(cls, code):
      enforce_not_blank(code, "Code")
      return cls(code = code)

   @classmethod
   def from_form(cls, form_data):
      return cls.composed_of(code=form_data.get('code'))
   
   def __str__(self):
        return self.code

   def synchronize_with(self,updated_promo_code):
      self.code = updated_promo_code.code
