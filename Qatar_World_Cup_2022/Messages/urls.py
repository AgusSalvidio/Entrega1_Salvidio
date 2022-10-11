from django.urls import path

from .views import chat_users,chat_between

urlpatterns = [
    path('', chat_users, name="chat_users"),
    path('chat_users/', chat_users, name="chat_users"),
    path('chat_between/<logged_user_id>/<receiver_user_id>', chat_between, name="chat_between"),
]
