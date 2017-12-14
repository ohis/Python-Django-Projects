from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show$', views.show),
    url(r'^register$', views.register),
    url(r'^add_new$', views.add_new, name = 'add_new'),
    url(r'^add$', views.create_item, name = 'create'),
    url(r'^delete/(?P<id>\d+)$',views.delete_item,name = 'rem')



]
