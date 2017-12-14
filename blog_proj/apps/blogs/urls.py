from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name ="index"),
    url(r'^blogs$',views.blogs),
    url(r'^show$',views.show),
    url(r'^comments/(?P<id>\d+)$',views.comments)

]
