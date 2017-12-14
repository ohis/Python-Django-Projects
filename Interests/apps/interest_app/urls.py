from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_index' ),
    url(r'^add$', views.add, name = 'users_page'),
    url(r'^back$',views.back_to_index, name = 'back'),
    url(r'^next$',views.back_to_next, name = 'next_page'),
    url(r'^show$',views.back_to_next, name = 'shows'),
    url(r'^show/(?P<id>\d+)$',views.show, name = 'show_page'),
    url(r'^delete/(?P<id>\d+)$',views.delete, name = 'remove_interest'),
]
