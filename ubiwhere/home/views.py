from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


"""  Lists the project's parts  """
def index(request):
	return HttpResponse('<h1>Ubiwhere</h1><br><br><br><a href="/api/">API</a><br><a href="/webapp/">Webapp</a><br><a href="/jsonparser/">JSON Parser</a>')