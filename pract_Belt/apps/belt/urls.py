from django.conf.urls import url
from . import views

#from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.log),
    url(r'^submit$', views.submit),
    url(r'^quotes$', views.show),
    url(r'^quotes/add/(?P<id>\d+)$', views.add_quote),
    url(r'^quotes/remove/(?P<id>\d+)$', views.remove)

]
