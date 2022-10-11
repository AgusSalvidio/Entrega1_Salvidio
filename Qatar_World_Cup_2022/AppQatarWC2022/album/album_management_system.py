from AppQatarWC2022.album.album import Album, AlbumPage
from AppQatarWC2022.countries.country import Country

from operator import attrgetter

class AlbumManagementSystem:
      
    def __init__(self):
        self.current_album = None
       
    def updated_album_using(self,generated_sticker_collection):
    
        qualified_countries = self.qualified_countries()
        
        album_page_collection = []
        for country in qualified_countries:
            stickers_filtered_by_country = list(filter(lambda generated_sticker: generated_sticker.country() == country,generated_sticker_collection))
            album_page = AlbumPage.composed_of(country,country.background(),stickers_filtered_by_country)
            album_page.initialize_slots()
            album_page_collection.append(album_page)

        return Album.composed_of(album_page_collection,album_page_collection[0])

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

    def countries(self):
        return Country.objects.all()

    def qualified_countries(self):
        return Country.objects.filter(qualified = True).order_by('name')

    def is_next_page_allowed(self):
        current_page = self.current_page()
        current_country = current_page.country()
                
        country_collection = country_collection = list(self.qualified_countries())
        current_country_index = country_collection.index(current_country)

        print(f"BBBBBB EL PAIS ES {current_country} SU INDICE ES {current_country_index}")
        if current_country_index >= 0 and current_country_index < (len(country_collection) - 1):
            return True
        else:
            return False

    def is_previous_page_allowed(self):
        current_page = self.current_page()
        current_country = current_page.country()
        
        country_collection = list(self.qualified_countries())
        current_country_index = country_collection.index(current_country)
        print(f"AAAAAAAA EL PAIS ES {current_country} SU INDICE ES {current_country_index}")
        
        if current_country_index > 0 and current_country_index < len(country_collection):
            return True
        else:
            return False

    def next_page(self):
        current_page = self.current_page()
        current_country = current_page.country()

        country_collection = list(self.qualified_countries())
        current_country_index = country_collection.index(current_country)
        
        if current_country_index >= 0 and current_country_index <  len(country_collection):
            next_country = country_collection[current_country_index + 1]
            next_page = self.page_for(next_country.full_name())

            return next_page
        else:
            return current_page
    
    def previous_page(self):
        current_page = self.current_page()
        current_country = current_page.country()

        country_collection = list(self.qualified_countries())
        current_country_index = country_collection.index(current_country)
        
        if current_country_index > 0 and current_country_index <  len(country_collection):
            previous_country = country_collection[current_country_index - 1]
            previous_page = self.page_for(previous_country.full_name())

            return previous_page
        else:
            return current_page


    def page_for(self,country_name):
        return self.album().page_for(country_name)

    def current_page(self):
        return self.album().current_page()

    def current_sticker_slot(self):
        return self.current_page().current_sticker_slot()