from AppQatarWC2022.album.album import Album, AlbumPage
from AppQatarWC2022.countries.country import Country


class AlbumManagementSystem:
      
    def __init__(self):
        self.current_album = None
       
    def refresh_album_with(self,generated_sticker_collection):
    
        qualified_countries = Country.objects.filter(qualified = True)
        
        album_page_collection = []
        for country in qualified_countries:
            stickers_filtered_by_country = list(filter(lambda generated_sticker: generated_sticker.country() == country,generated_sticker_collection))
            album_page = AlbumPage.composed_of(country,country.background(),stickers_filtered_by_country)
            album_page.initialize_slots()
            album_page_collection.append(album_page)

        self.update_album_with(Album.composed_of(album_page_collection,album_page))

    def update_album_with(self,album):
        self.current_album = album

    def album(self):
        return self.current_album

    def sticker_slot_image_at(self,slot_position):
        return self.album().sticker_slot_image_at(slot_position)

    def name(self):
        return 'Sistema de Administración de Álbum'

    def class_knownledge(self):
        return ['Album','AlbumPage']