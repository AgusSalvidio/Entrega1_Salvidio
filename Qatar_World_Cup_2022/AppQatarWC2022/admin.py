from django.contrib import admin
from .models import*

admin.site.register(PlayerSticker)
admin.site.register(LogoSticker)
admin.site.register(PlayerPosition)
admin.site.register(UserProfile)
admin.site.register(Country)
#Only for testing, then this should be removed
admin.site.register(GeneratedPlayerSticker)
admin.site.register(GeneratedLogoSticker)
admin.site.register(Article)