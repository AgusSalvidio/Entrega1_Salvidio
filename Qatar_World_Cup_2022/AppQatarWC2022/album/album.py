
from AppQatarWC2022.stickers.generated_sticker import GeneratedSticker


class Album:
    def __init__(self,album_page_collection,selected_page):
        self.album_page_collection = album_page_collection
        self.selected_page = selected_page

    @classmethod
    def composed_of(cls,album_page_collection,selected_page):

        return cls(
            album_page_collection = album_page_collection,
            selected_page = selected_page)
    
    def pages(self):
        return self.album_page_collection

    def current_page(self):
        return self.selected_page  
   
    def page_for(self,country_name):
        return list(filter(lambda album_page : album_page.country().full_name() == country_name,self.pages()))[0]

    def update_current_album_page_with(self, album_page):
        self.selected_page = album_page

class AlbumPage:
    def __init__(self,current_country,background_image,sticker_collection):
        self.background_image = background_image
        self.sticker_collection = sticker_collection
        self.current_country = current_country
        self.album_slots = {}
        self.current_index_position = 0

    @classmethod
    def composed_of(cls,current_country,background_image,sticker_collection):

        return cls(
            current_country = current_country,
            background_image = background_image,
            sticker_collection = sticker_collection)

    def sticker_slot_image_at(self,slot_position):
        return self.sticker_slot_at(slot_position).sticker()
    
    def sticker_slot_at(self,slot_position):
        return self.slots().get(slot_position)

    def slots(self):
        return self.album_slots

    def stickers(self):
        return self.sticker_collection
    
    def add_sticker_slot(self,sticker_slot):
        slot_position = sticker_slot.sticker().slot_position()
        self.album_slots.update({slot_position:sticker_slot})

    def index_position(self):
        return self.current_index_position

    def increment_index_position(self):
        self.current_index_position += 1

    def current_sticker_slot(self):
        return self.sticker_slot_at(self.current_index_position)

    def initialize_slots(self):
        
        generated_stickers = self.stickers()

        for slot_position in range(12):
            
            generated_sticker_in_slot = list(filter(lambda generated_sticker: generated_sticker.slot_position() == slot_position,generated_stickers))
                        
            if len(generated_sticker_in_slot) == 0:
                sticker_slot = EmptySlot(GeneratedSticker.for_empty_slot_in(slot_position))
            elif generated_sticker_in_slot[0].category() == 'Glued':
                sticker_slot = GluedSlot(generated_sticker_in_slot[0])
            else:
                sticker_slot = NewSlot(generated_sticker_in_slot[0])
                
            self.add_sticker_slot(sticker_slot)

    def country(self):
        return self.current_country

    def glue_sticker(self,sticker_id):
        sticker = list(filter(lambda generated_sticker: generated_sticker.id == sticker_id,self.stickers() ))[0]
        sticker.glue_sticker()
        

class StickerSlot:
    def __init__(self,generated_sticker):
        self.generated_sticker = generated_sticker
    
    def sticker(self):
        return self.generated_sticker

    def sticker_image(self):
        return self.sticker().sticker_image()

    def is_glued(self):
        return False

    def is_new(self):
        return False

    def is_empty(self):
        return False
    
class NewSlot(StickerSlot):
    
    def sticker_image(self):
        return '/media/stickers/to-add.jpg'

    def is_new(self):
        return True

class GluedSlot(StickerSlot):
    
    def is_glued(self):
        return True

class EmptySlot(StickerSlot):

    def sticker_image(self):
        return '/media/stickers/not-found.jpg'

    def is_empty(self):
        return True
