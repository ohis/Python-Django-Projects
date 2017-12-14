from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^remove/(?P<id>\d+)$',views.remove),
    url(r'^del/(?P<id>\d+)$',views.destroy)
]
