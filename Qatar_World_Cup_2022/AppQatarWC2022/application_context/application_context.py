
class ApplicationContext:
    def __init__(self,system_collection):
        self.system_collection = system_collection
        self.form = None
        self.selected_object = None
        self.message = ''

    @classmethod
    def implementing(cls,system_collection):
        return cls(system_collection = system_collection)

    def systems(self):
        return self.system_collection

    def filter_system_named(self,system_name):
        return list(filter(lambda system: system.name() == system_name,self.systems() ))[0] 

    def user_system(self):
        return self.filter_system_named('Sistema de Administración de Usuarios') 
    def sticker_system(self):
        return self.filter_system_named('Sistema de Administración de Stickers')
    def album_system(self):
        return self.filter_system_named('Sistema de Administración de Álbum')
    def promo_code_system(self):
        return self.filter_system_named('Sistema de Administración de Códigos Promocionales')  
        
    def current_form(self):
        return self.form

    def current_object(self):
        return self.selected_object
    
    def current_message(self):
        return self.message

    def update_form_with(self,form):
        self.form = form

    def update_selected_object_with(self,object):
        self.selected_object = object

    def update_information_message_with(self,message):
        self.message = message

    def logged_user(self):
        return self.user_system().logged_user()

    def logged_user_profile_avatar(self):
        return self.user_system().logged_user_profile_avatar()

    def store_logged_user(self,user):
        self.user_system().store_logged_user(user)

    def stickers_of(self,user):
        return self.sticker_system().stickers_of(user)

    def refresh_album(self):
        user = self.logged_user()
        user_sticker_collection = self.stickers_of(user) 
        self.album_system().refresh_album_with(user_sticker_collection)

    def sticker_slot_image_at(self,slot_position):
        return self.slots().get(slot_position).sticker_image()

    def slots(self):
        return self.album().current_page().slots()
    
    def album(self):
        return self.album_system().album()

    def current_page(self):
        return self.album().current_page()

    def sticker_first_row_range(self):
        return list(range(6))

    def sticker_second_row_range(self):
        return list(range(6,12))

    def increment_index_position(self):
        self.current_page().increment_index_position()

    #This function is needed when html loads the url path, its a horrible implementation but jinja does not allow functions with arguments.
    def next_sticker_image(self):
        current_index = self.current_page().index_position()
        image = self.sticker_slot_image_at(current_index)
        self.increment_index_position()
        return image

    """ Promo Codes """
    def promo_codes(self):
        return self.promo_code_system().promo_codes()

    def register_promo_code(self,promo_code):
        self.promo_code_system().register_promo_code(promo_code)

    def promo_code_identified_as(self,promo_code_id):
        return self.promo_code_system().promo_code_identified_as(promo_code_id)

    def unregister_promo_code(self,promo_code):
        self.promo_code_system().unregister_promo_code(promo_code)

    def update_promo_code_with(self,promo_code,updated_promo_code):
        self.promo_code_system().update_promo_code_with(promo_code,updated_promo_code)

    """ Player Sticker """
    def player_stickers(self):
        return self.sticker_system().player_stickers()

    def register_player_sticker(self,player_sticker):
        self.sticker_system().register_player_sticker(player_sticker)

    def player_sticker_identified_as(self,player_sticker_id):
        return self.sticker_system().player_sticker_identified_as(player_sticker_id)

    def unregister_player_sticker(self,player_sticker):
        self.sticker_system().unregister_player_sticker(player_sticker)

    def update_player_sticker_with(self,player_sticker,updated_player_sticker):
        self.sticker_system().update_player_sticker_with(player_sticker,updated_player_sticker)