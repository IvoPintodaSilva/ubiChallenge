"""ubiwhere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
"""  Argument for user is the e-mail, which is the PK of the user  """
urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
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


urlpatterns = format_suffix_patterns(urlpatterns)