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

    def update_current_album_page_with(self,album_page):
        self.album().update_current_album_page_with(album_page)

    def album(self):
        return self.current_album

    def sticker_slot_image_at(self,slot_position):
        return self.album().sticker_slot_image_at(slot_position)

    def name(self):
        return 'Sistema de Administración de Álbum'

    def class_knownledge(self):
        return ['Album','AlbumPage']

    def qualified_countries(self):
        print(f"{Country.objects.filter(qualified = True)}")
        return Country.objects.filter(qualified = True)

    def next_page_is_allowed(self):
        page_collection = self.album().pages()
        current_page = self.album().current_page()
        
        current_page_index = page_collection.index(current_page)

        if current_page_index >= 0 and current_page_index <  len(page_collection):
            return True
        else:
            return False
    
    def previous_page_is_allowed(self):
        page_collection = self.album().pages()
        current_page = self.album().current_page()
        
        current_page_index = page_collection.index(current_page)

        if current_page_index > 0 and current_page_index <  len(page_collection):
            return True
        else:
            return False

    def next_page(self):
        current_page = self.album().current_page()
        if self.next_page_is_allowed():
            page_collection = self.album().pages()
            next_page_index = page_collection.index(current_page) + 1
            next_page = page_collection[next_page_index]
            return next_page
        else:
            return current_page
        
    def previous_page(self):
        current_page = self.album().current_page()
        if self.previous_page_is_allowed():
            page_collection = self.album().pages()
            previous_page_index = page_collection.index(current_page) - 1
            previous_page = page_collection[previous_page_index]
            return previous_page
        else:
            return current_page

    def page_for(self,country_name):
        return self.album().page_for(country_name) 