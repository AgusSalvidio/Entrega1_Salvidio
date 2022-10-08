from django.apps import AppConfig

from .application_context import ApplicationContext


class Appqatarwc2022Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppQatarWC2022'
    context = None
    sticker_system = None
    user_system = None
    album_system = None

    def ready(self):
        from .stickers import StickerManagementSystem
        from .users import UserManagementSystem
        from .album import AlbumManagementSystem
        from .promo_codes import PromoCodeManagementSystem
        self.sticker_system = StickerManagementSystem()
        self.user_system = UserManagementSystem()
        self.album_system = AlbumManagementSystem()
        self.promo_code_system = PromoCodeManagementSystem()
        self.context = ApplicationContext.implementing([self.sticker_system,self.user_system,self.album_system,self.promo_code_system])

    def working_context(self):
        return self.context
    
    