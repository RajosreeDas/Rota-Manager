from django.conf.urls import url
from . import views 

app_name='meeting'

urlpatterns=[
    
    url(r'^$', views.index, name='index'),
    
    #create_meeting
    url(r'^create_meeting', views.create_meeting, name='create_meeting'),
    
    #details
    url(r'^(?P<meeting_id>[0-9]+)/$', views.meeting_details, name='meeting_details'),
    
    #edit_meeting
    url(r'^(?P<meeting_id>[0-9]+)/$', views.edit_meeting, name='edit_meeting'),
    
    #delete_meeting
    url(r'^(?P<meeting_id>[0-9]+)/$', views.delete_meeting, name='delete_meeting')]












