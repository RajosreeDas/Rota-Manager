from django.conf.urls import url
from .import views



app_name='Account'

urlpatterns = [
    url(r'^$', views.index, name='index'),

	# /accounts/register/
	url(r'^register/', views.user_register, name='register'),

	#/Account/login
	url(r'^login/', views.user_login, name='login'),

	#/Account/edit-user
	url(r'^(?P<user_id>[0-9]+)/edit_user/', views.edit_user, name='user-edit'),

    #delete
	url(r'^(?P<user_id>[0-9]+)/delete_user/', views.edit_user, name='delete-user'),

    #profile
	url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),

    #logout
	url(r'^logout/$', views.user_logout, name='logout'),

]