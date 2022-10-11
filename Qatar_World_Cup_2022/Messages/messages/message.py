from django.conf import settings
from django.db import models

from AppQatarWC2022.users.user_profile import UserProfile


class Message(models.Model):
    sender = models.OneToOneField(UserProfile,related_name='sender',on_delete=models.CASCADE)
    receiver = models.OneToOneField(UserProfile,related_name='receiver',on_delete=models.CASCADE)
    was_read = models.BooleanField()
    date = models.DateTimeField()
    content = models.TextField()

    @classmethod
    def from_form(cls, sender, date, form_data):
        receiver = form_data.get('receiver')
        content = form_data.get('content')
        return cls(sender=sender, receiver=receiver, date=date, content=content)

    def sender_username(self):
        return self.sender.username()

    def receiver_username(self):
        return self.receiver.username()

    def __str__(self):
        return f'Mensaje de {self.sender_username()} para {self.receiver_username()} el {self.formatted_date_and_time_sent()}'

    def formatted_date(self):
        return self.date.strftime("%d/%m/%Y %H:%M:%S")




