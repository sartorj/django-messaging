from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Mailbox(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    num_messages = models.IntegerField()
    max_messages = models.IntegerField()
    public_key = models.CharField(max_length=2048, default='NO KEY')

    def __str__(self):
        return self.public_key

class Message(models.Model):
    box = models.ForeignKey(Mailbox, on_delete=models.CASCADE)
    date_sent = models.DateField()
    message = models.CharField(max_length=245) #max length of 2048 RSA message                         
    def __str__(self):
        return self.message

