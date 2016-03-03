from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


def index(request):
    #return HttpResponse("You are at the webmessage index")
    return render(request, 'webmessage/index.html')

def mailbox(index):
    return HttpResponse("You are at the mailbox index")

def detail(request,user_name):

    return HttpResponse("You're looking at the mailbox of %s." % user_name)

def sending(request, receiving_user):
    return HttpResponse("You're sending a message to:  %s." % receiving_user)


def users(request):
    recent_user_list = User.objects.order_by('-username')
    template = loader.get_template('webmessage/userindex.html')
    context = {
        'recent_user_list' : recent_user_list,
    }
    
    return HttpResponse(template.render(context,request))


def register(request):
    context = {}
    return render(request, 'webmessage/register.html')
