from django.shortcuts import redirect
from AppQatarWC2022.users.user_profile import UserProfile
from Messages.messages import Message
from AppQatarWC2022.models import app
from django.apps import apps


class MessageManagementSystem:

    def __init__(self):
        self.messages_repository = Message.objects
        self.users_repo = UserProfile.objects
        self.logged_user_repo = None

    def user_identified_as(self,user_id):
        return self.users_repo.get(id = user_id)

    def chat_users(self):
        all_users = self.users_repo.all()
        return list(filter(lambda user: user.internal_user != self.logged_user().internal_user,all_users))

    def logged_user(self):
        return self.logged_user_repo

    def logged_user_profile_avatar(self):
        if self.logged_user() == None:
            #return '/media/avatars/default_avatar.jpg'
            return redirect('login')
        else:
            return self.logged_user().avatar()

    def is_user_logged(self):
        if self.logged_user_repo == None:
            return False
        else:
            return True

    def users(self):
        return self.users_repo.all()

    def store_logged_user(self,user):
        self.logged_user_repo = (self.users_repo.get(internal_user = user))

    def messages(self):
        return list(self.messages_repository.all())

    def send_new_message(self, message):
        print(f"{message}")
        message.save()

    def messages_from(self, sender, receiver):
        return self.messages_repository.filter(sender=sender).filter(receiver=receiver)

    def conversation_between(self, user, another_user):
        messages_sent_by_user = self.messages_from(user, receiver=another_user)
        messages_received_by_user = self.messages_from(another_user, receiver=user)
        messages = messages_sent_by_user | messages_received_by_user
        return messages.order_by('date_time')
