from .player_sticker import PlayerSticker
from .logo_sticker import LogoSticker
from .generated_player_sticker import GeneratedPlayerSticker
from .generated_logo_sticker import GeneratedLogoSticker

class StickerManagementSystem:

    def __init__(self):
        self.player_stickers_repo = PlayerSticker.objects
        self.logo_stickers_repo = LogoSticker.objects
        self.generated_player_stickers_repo = GeneratedPlayerSticker.objects
        self.generated_logo_stickers_repo = GeneratedLogoSticker.objects

    def player_stickers(self):
        return self.player_stickers_repo.all()
    
    def logo_stickers(self):
        return self.logo_stickers_repo.all()
    
    def generated_player_stickers(self):
        return self.generated_player_stickers_repo
    
    def generated_logo_stickers(self):
        return self.generated_logo_stickers_repo

    def stickers_of(self,user):
        generated_player_sticker_collection = list(self.generated_player_stickers().filter(owner = user))
        generated_logo_sticker_collection = list(self.generated_logo_stickers().filter(owner = user))
        return generated_player_sticker_collection + generated_logo_sticker_collection

    def generate_sticker_pack(self):
        pass

    def name(self):
        return 'Sistema de Administración de Stickers'    

    def register(self,sticker):
        sticker.save()

    def generated_sticker_of(self,generated_sticker_id):
        return self.generated_stickers_repo.get(id = generated_sticker_id)

    def identified_player_as(self,player_sticker_id):
        return self.player_stickers_repo.get(id = player_sticker_id)
    
    def identified_logo_as(self,logo_sticker_id):
        return self.logo_stickers_repo.get(id = logo_sticker_id)

    def unregister(self,sticker):
        sticker.delete()
    
    def assert_there_is_no_sticker_identified_as(self, full_name):
        pass

    def update_with(self,sticker,updated_sticker):
        if sticker.full_name() != updated_sticker.full_name():
            self.assert_there_is_no_sticker_identified_as(updated_sticker.full_name())
        sticker.synchronize_with(updated_sticker)
        sticker.save()

    def class_knownledge(self):
        return ['PlayerSticker','GeneratedSticker','LogoSticker','GeneratedPlayerSticker','GeneratedLogoSticker']