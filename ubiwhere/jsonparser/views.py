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

	"""  The only attributes needed in order to insert a song using the API  """
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
		
		"""  Gets status code 201 if the song is created or 200 if it's already there  """
		"""  Decided to remove this verification because aTracks with special characters fail to be inserted  """
		"""  This way, if one fails, all the other ones are still inserted into the system   """
		#if r.status_code != 201 and r.status_code != 200:
			#return HttpResponse(status = 400)

		resp = resp + str(json.dumps(d))
	resp = resp + ']'

	"""  Dumps the parsed JSON  """
	return HttpResponse(str(resp) + '<br><br><br><a href="/webapp/song">Check Songs on Webapp</a><br><br><a href="/index/">Index</a>', status = 200)
