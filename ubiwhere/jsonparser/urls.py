from django.conf.urls import include, url
from jsonparser import views


"""  URL defined for json parser. Just /jsonparser/ is enough because it's the only method of this app  """
urlpatterns = [
    url(r'^$', views.parse_json),
]


