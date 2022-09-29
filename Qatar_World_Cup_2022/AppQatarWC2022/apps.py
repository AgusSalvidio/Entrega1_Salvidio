from django.apps import AppConfig


class Appqatarwc2022Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProcessKnownledge'
    sticker_system = None
    user_system = None

    def ready(self):
        from .stickers import StickerManagementSystem
        from .users import UserManagementSystem
        self.sticker_system = StickerManagementSystem()
        self.user_system = UserManagementSystem()