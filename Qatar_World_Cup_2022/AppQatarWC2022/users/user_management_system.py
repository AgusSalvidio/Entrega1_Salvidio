from .user_profile import UserProfile

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