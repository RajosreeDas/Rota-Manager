from django.conf.urls import url 
from . import views


App_Name='dashboard'

urlpatterns = [
     
     #index
     url(r'^$', views.index, name='index')
]
