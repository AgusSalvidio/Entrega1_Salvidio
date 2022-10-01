
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
        return filter(lambda album_page: album_page.country().name == country_name,self.pages)

    def glue_sticker(self,sticker_id):
        self.current_page().glue_sticker(sticker_id)  

class AlbumPage:
    def __init__(self,country_name,background_image,sticker_slot_collection):
        self.background_image = background_image
        self.sticker_slot_collection = sticker_slot_collection
        self.country_name = country_name
        self.album_slots = {}

    @classmethod
    def composed_of(cls,country,background_image,sticker_slot_collection):

        return cls(
            country = country,
            background_image = background_image,
            sticker_slot_collection = sticker_slot_collection)

    def stickers(self):
        return self.sticker_slot_collection
    
    def add_sticker_slot(self,sticker_slot):
        self.album_slots.update({sticker_slot.slot_position():sticker_slot})

    #Revisar de pedirselo al workingContext 
    def initialize_slots(self):
        for sticker_slot in self.stickers():
            self.add_sticker_slot(sticker_slot)

    def country(self):
        return self.country_name

    def glue_sticker(self,sticker_id):
        filter(lambda sticker: sticker.id == sticker_id,self.stickers).glue_sticker()

class StickerSlot:
    def __init__(self,generated_sticker):
        self.generated_sticker = generated_sticker
    
    def sticker(self):
        return self.generated_sticker

    def isGlued(self):
        return False

    def isNew(self):
        return False

    def isEmpty(self):
        return False
    
class NewSlot(StickerSlot):
   
    def isNew(self):
        return True

class GluedSlot(StickerSlot):
    
    def isGlued(self):
        return True

class EmptySlot(StickerSlot):

    def isEmpty(self):
        return True
