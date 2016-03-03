from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("You are at the webmessage index")

def detail(request):
    return HttpResponse("You're looking at the mailbox of %s." % request.user)

def sending(request, receiving_user):
    return HttpResponse("You're sending a message to:  %s." % receiving_user)
