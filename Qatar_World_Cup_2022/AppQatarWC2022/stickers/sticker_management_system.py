from .player_sticker import PlayerSticker
from .generated_sticker import GeneratedSticker

class StickerManagementSystem:

    def __init__(self):
        self.player_stickers_repo = PlayerSticker.objects
        self.generated_stickers_repo = GeneratedSticker.objects

    def generated_stickers(self):
        return self.generated_stickers_repo

    def stickers_of(self,user):
        return  self.generated_stickers().filter(owner = user)

    def generate_sticker_pack(self):
        pass

    def name(self):
        return 'Sistema de Administración de Stickers'    


    