from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='my_index'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='new_client'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^(?P<id>\d+)/addProject$', views.addProject, name='new_project'),
]
