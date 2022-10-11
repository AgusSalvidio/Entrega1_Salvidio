from django.contrib import admin
from .models import*

admin.site.register(PlayerSticker)
admin.site.register(PlayerPosition)
admin.site.register(PromoCode)
admin.site.register(UserProfile)
admin.site.register(Country)
#Only for testing, then this should be removed
admin.site.register(GeneratedSticker)
admin.site.register(Article)