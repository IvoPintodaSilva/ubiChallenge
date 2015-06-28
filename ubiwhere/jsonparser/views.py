# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import requests
import json
import urllib
import urllib2

"""  Method that parses a json string received and POSTs the info into the system  """
"""  API accepts JSON so it returns the parsed data in JSON format as well  """
def parse_json(request):
	json_data = requests.get('http://freemusicarchive.org/recent.json')
	data = json.loads(json_data.content)

	d = {'title': '', 'artist': '', 'album': ''}
	resp = '['
	for track in data['aTracks']:
		if resp != '[':
			resp = resp + ','

		d['title'] = track['track_title']
		d['artist'] = track['artist_name']
		d['album'] = track['album_title']

		"""  POSTs the data into the system using the API  """
		r = requests.post('http://ivopintodasilva.herokuapp.com/api/add_song/', data = json.dumps(d), headers={'content-type': 'application/json; charset=utf-8'})
		
		if r.status_code != 201 and r.status_code != 200:
			return HttpResponse(status = 400)
		resp = resp + str(json.dumps(d))
	resp = resp + ']'
	return HttpResponse(str(resp), status = 200)
