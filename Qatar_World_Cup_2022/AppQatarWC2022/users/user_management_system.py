from django.shortcuts import redirect
from .user_profile import UserProfile
from AppQatarWC2022.users.forms import UserRegistration

class UserManagementSystem:

    def __init__(self):
        self.users_repo = UserProfile.objects
        self.logged_user_repo = None

    def logged_user(self):
        return self.logged_user_repo

    def users(self):
        return self.users_repo.all()

    def store_logged_user(self,user):
        self.logged_user_repo = (self.users_repo.get(internal_user = user))

    def name(self):
        return 'Sistema de Administración de Usuarios'

    def logged_user_profile_avatar(self):
        if self.logged_user() == None:
            #return '/media/avatars/default_avatar.jpg'
            return redirect('login')
        else:
            return self.logged_user().avatar()
    
    def register(self, user_profile):
        user_profile.save()

    def update_with(self,user_profile,updated_user_profile):
        """if user_profile.name() != updated_user_profile.name():
            self.assert_there_is_no_player_sticker_identified_as(updated_player_sticker.name())"""
        user_profile.synchronize_with(updated_user_profile)
        user_profile.save()

    def class_knownledge(self):
        return ['UserProfile','UserRegistration']
       