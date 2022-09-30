from django.apps import AppConfig


class Appqatarwc2022Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppQatarWC2022'
    sticker_system = None
    user_system = None
    album_system = None

    def ready(self):
        from .stickers import StickerManagementSystem
        from .users import UserManagementSystem
        from .album import AlbumManagementSystem
        self.sticker_system = StickerManagementSystem()
        self.user_system = UserManagementSystem()
        self.album_system = AlbumManagementSystem()