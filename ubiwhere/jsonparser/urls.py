from django.conf.urls import include, url
from jsonparser import views

urlpatterns = [
    url(r'^parse/$', views.parse_json),
]


