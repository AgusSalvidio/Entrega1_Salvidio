from django.shortcuts import redirect
import pexpect
from AppQatarWC2022.stickers import generated_sticker
from .player_sticker import PlayerSticker
from .logo_sticker import LogoSticker
from .generated_player_sticker import GeneratedPlayerSticker
from .generated_logo_sticker import GeneratedLogoSticker
from AppQatarWC2022.countries import Country

import random

class StickerManagementSystem:

    def __init__(self):
        self.player_stickers_repo = PlayerSticker.objects
        self.logo_stickers_repo = LogoSticker.objects
        self.generated_player_stickers_repo = GeneratedPlayerSticker.objects
        self.generated_logo_stickers_repo = GeneratedLogoSticker.objects
        self.rarities = self.rarity_probalities()

    def player_stickers(self):
        return self.player_stickers_repo.all()
    
    def logo_stickers(self):
        return self.logo_stickers_repo.all()

    def generated_sticker_of(self,id,object_class):
        if object_class == 'GeneratedPlayerSticker':
            return self.generated_player_stickers_repo.get(id = id)
        else:
            return self.generated_logo_stickers_repo.get(id = id)
            
    def generated_player_stickers(self):
        return self.generated_player_stickers_repo
    
    def generated_logo_stickers(self):
        return self.generated_logo_stickers_repo

    def stickers_of(self,user):
        generated_player_sticker_collection = list(self.generated_player_stickers().filter(owner = user))
        generated_logo_sticker_collection = list(self.generated_logo_stickers().filter(owner = user))
        return generated_player_sticker_collection + generated_logo_sticker_collection

    def name(self):
        return 'Sistema de Administración de Stickers'    

    def register(self,sticker):
        sticker.save()

    def identified_as(self,sticker_id,object_class):
        if object_class == 'PlayerSticker':
            return self.player_stickers_repo.get(id = sticker_id)
        elif object_class == 'LogoSticker':
            return self.logo_stickers_repo.get(id = sticker_id)
        else:
            return Country.objects.get(id = sticker_id)
    
    def unregister(self,sticker):
        sticker.delete()
    
    def assert_there_is_no_sticker_identified_as(self, full_name):
        pass

    def update_with(self,sticker,updated_sticker):
        if sticker.full_name() != updated_sticker.full_name():
            self.assert_there_is_no_sticker_identified_as(updated_sticker.full_name())
        sticker.synchronize_with(updated_sticker)
        sticker.save()

    def rarity_probalities(self):
        rarity_prob = {
            range(1,81):'Común',
            range(80,96):'Épica',
            range(96,101):'Legendaria'}
        return rarity_prob

    def filter_stickers_using(self,stickers,rarity):
        return list(stickers.filter(rarity_category = rarity))

    def sticker_for(self,user,rarity_category):
        sticker_type_number = random.randint(1,100)
        filtered_stickers = []
        if sticker_type_number <= 85:
            filtered_stickers = self.filter_stickers_using(self.player_stickers_repo,rarity_category)
            filtered_stickers_quantity = len(filtered_stickers) - 1
            if filtered_stickers_quantity >= 0:
                sticker_number = random.randint(0,filtered_stickers_quantity)
            else:
                pass
            sticker_template = filtered_stickers[sticker_number]
            generated_sticker = GeneratedPlayerSticker.belonging_to(user,sticker_template,'New')
            return generated_sticker
            
        else:
            filtered_stickers = self.filter_stickers_using(self.logo_stickers_repo,rarity_category)
            filtered_stickers_quantity = len(filtered_stickers) - 1
            if filtered_stickers_quantity >= 0:
                sticker_number = random.randint(0,filtered_stickers_quantity)
            else:
                pass
            sticker_template = filtered_stickers[sticker_number]
            generated_sticker = GeneratedLogoSticker.belonging_to(user,sticker_template,'New')
            return generated_sticker
        
    def sticker_pack_for(self,user):
        rarity_dictionary = self.rarities
        generated_stickers = []
        for sticker in range(5):
            rarity_number = random.randint(1,100)
            for rarity_number_collection in rarity_dictionary.keys():
                    if rarity_number in rarity_number_collection:
                        rarity_category = rarity_dictionary[rarity_number_collection]
                        generated_sticker = self.sticker_for(user,rarity_category)
                        generated_sticker.save()
                        generated_stickers.append(generated_sticker)
                        break
        return generated_stickers
        
    def class_knownledge(self):
        return ['PlayerSticker','GeneratedSticker','LogoSticker','GeneratedPlayerSticker','GeneratedLogoSticker','Country']