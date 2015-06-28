from django.conf.urls import include, url
from webapp import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^user/$', views.user),
	url(r'^song/$', views.song),
	url(r'^user/delete/$', views.user_delete),
	url(r'^user/form/$', views.user_form),
	url(r'^user/add/$', views.user_add),
	url(r'^user/details/$', views.user_details),
	url(r'^song/delete/$', views.song_delete),
	url(r'^song/form/$', views.song_form),
	url(r'^song/add/$', views.song_add),
	url(r'^song/details/$', views.song_details),
	url(r'^likes/$', views.likes),
	url(r'^likes/form/$', views.likes_form),
	url(r'^likes/delete/$', views.likes_delete),
	url(r'^likes/add/$', views.likes_add),
	url(r'^likes/add_onuserdetails/$', views.likes_add_onuserdetails),


	
]

