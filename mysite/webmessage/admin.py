from django.contrib import admin

# Register your models here.

from .models import Mailbox, Message


admin.site.register(Mailbox)
admin.site.register(Message)
