from django.conf.urls import url 
from .import views

app_name='Events'

urlpatterns= [
    #index
    url(r'^$', views.index, name='index'),

    #create_event
    url(r'^Create_Event', views.create_event, name='create_event'),

    #details
    url(r'^(?P<event_id>[0-9]+)/$', views.details, name='event_details'),

    #delete_event
    url(r'^(?P<event_id>[0-9]+)/$', views.delete_event, name='delete_event'),

    #event_edit
    url(r'^(?P<event_id>[0-9]+)/$', views.edit_event, name='edit_event')
]