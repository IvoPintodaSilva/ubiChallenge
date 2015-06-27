from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import urllib2
import json


def parse_json(request):
	serialized_data = urllib2.urlopen('http://freemusicarchive.org/recent.json').read()
	data = json.loads(serialized_data)
	print data
	return HttpResponse(str(data))

