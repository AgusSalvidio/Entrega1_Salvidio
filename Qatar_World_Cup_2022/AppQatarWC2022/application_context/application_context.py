class ApplicationContext:
    def __init__(self,system_collection):
        self.system_collection = system_collection
        self.form = None
        self.message = ''

    @classmethod
    def implementing(cls,system_collection):
        return cls(system_collection = system_collection)

    def systems(self):
        return self.system_collection

    def user_system(self):
        return next((system for system in self.systems() if system.name() == 'Sistema de Administración de Usuarios'),None)

    def sticker_system(self):
        return next((system for system in self.systems() if system.name() == 'Sistema de Administración de Stickers'),None)
    
    def album_system(self):
        return next((system for system in self.systems() if system.name() == 'Sistema de Administración de Álbum'),None)
                
    def current_form(self):
        return self.form
    
    def current_message(self):
        return self.message

    def update_form_with(self,form):
        self.form = form

    def update_information_message_with(self,message):
        self.message = message

    def logged_user(self):
        return self.user_system().logged_user()

    def logged_user_profile_avatar(self):
        return self.user_system().logged_user_profile_avatar()

    def store_logged_user(self,user):
        self.user_system().store_logged_user(user)
        