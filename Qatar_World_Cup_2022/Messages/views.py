from datetime import datetime

from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Messages.messages import Message
from Messages.forms import MessageRegistration


message_system = apps.get_app_config('Messages').message_management_system

working_context = {'working_context':message_system}

@login_required
def chat_users(request):
    message_system.store_logged_user(request.user)
    return render(request,'chat_users.html',working_context)

@login_required
def chat_between(request,logged_user_id,receiver_user_id):
    messages = message_system.conversation_between(logged_user_id,receiver_user_id)
    receiver_user = message_system.user_identified_as(receiver_user_id)
    context = {'working_context':message_system,'messages':messages,'receiver_user':receiver_user}
    return render(request,'chat_between.html',context)