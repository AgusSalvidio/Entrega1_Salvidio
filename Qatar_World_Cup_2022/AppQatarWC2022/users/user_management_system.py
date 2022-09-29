from .user_profile import UserProfile

class UserManagementSystem:

    def __init__(self):
        self.users_repository = UserProfile.objects
        self.logged_user_repo = None

    def logged_user(self):
        return self.logged_user_repo

    def users(self):
        return self.users_repository.all()

    def store_logged_user(self,user):
        self.logged_user_repo = (self.users_repository.get(internal_user = user))