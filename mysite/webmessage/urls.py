from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^mailbox/$', views.detail, name='detail'),
    # ex: /polls/5/vote/
    url(r'^(?P<receiving_user>[0-9]+)/sending/$', views.sending, name='sending'),
]
