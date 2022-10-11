from .player_sticker import PlayerSticker
from .generated_sticker import GeneratedSticker

class StickerManagementSystem:

    def __init__(self):
        self.player_stickers_repo = PlayerSticker.objects
        self.generated_stickers_repo = GeneratedSticker.objects

    def player_stickers(self):
        return self.player_stickers_repo.all()
    
    def generated_stickers(self):
        return self.generated_stickers_repo

    def stickers_of(self,user):
        return  self.generated_stickers().filter(owner = user)

    def generate_sticker_pack(self):
        pass

    def name(self):
        return 'Sistema de Administración de Stickers'    

    def register(self,player_sticker):
        player_sticker.save()

    def generated_sticker_of(self,generated_sticker_id):
        return self.generated_stickers_repo.get(id = generated_sticker_id)

    def identified_as(self,player_sticker_id):
        return self.player_stickers_repo.get(id = player_sticker_id)

    def unregister(self,player_sticker):
        player_sticker.delete()
    
    def assert_there_is_no_player_sticker_identified_as(self, full_name):
        pass

    def update_with(self,player_sticker,updated_player_sticker):
        if player_sticker.full_name() != updated_player_sticker.full_name():
            self.assert_there_is_no_player_sticker_identified_as(updated_player_sticker.full_name())
        player_sticker.synchronize_with(updated_player_sticker)
        player_sticker.save()

    def class_knownledge(self):
        return ['PlayerSticker','GeneratedSticker']