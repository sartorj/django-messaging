from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /webmessage/
    url(r'^$', views.index, name='index'),
    # ex: /webmessage/mailbox/
    url(r'^mailbox/$', views.mailbox, name='mailbox'),
    # ex: /webmessage/mailbox/<username>
    url(r'^mailbox/(?P<user_name>[^/]+)/$', views.detail, name='detail'),
    # ex: /polls/5/vote/
    url(r'^(?P<receiving_user>[0-9]+)/sending/$', views.sending, name='sending'),
    # ex: /webmessage/users/
    url(r'^users/$', views.users, name='users'),
    # ex: /webmessage/register/
    url(r'^register/$', views.register, name = 'register'),

]
