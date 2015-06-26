from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

"""  Argument for user is the e-mail, which is the PK of the user  """
urlpatterns = [
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^', include('api.urls')),
    url(r'^list_user/$', views.user_list),
    url(r'^add_user/', views.add_user),
    url(r'^user/(?P<email>[a-z0-9]+@[a-z]+.[a-z]+)$', views.user),
    url(r'^list_song/$', views.song_list),
    url(r'^add_song/', views.add_song),
    url(r'^song/(?P<songid>[0-9]+)$', views.song),
    url(r'^list_likes/$', views.likes_list),
    url(r'^add_likes/', views.add_likes),
]


