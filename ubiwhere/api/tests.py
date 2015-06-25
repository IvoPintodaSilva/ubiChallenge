from django.test import TestCase
from api.models import User, Song, Likes
from rest_framework import status

"""  Library for testing. Provides a way to act like a dummy web browser.  """
"""  All DB tables and instances created from these tests are temporary and removed in the end of the tests  """
from rest_framework.test import APIClient




class APITestCase(TestCase):
	client = APIClient()

	"""  Test that POSTs 4 users into the system  """
	def test_add_users(self):
		"""  Invoke REST method to add a user  """
		r = self.client.post('/add_user/', {'email': 'ernesto@gmail.com', 'name': 'Ernesto Valverde'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_user/', {'email': 'rufino@gmail.com', 'name': 'Joao Rufino'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_user/', {'email': 'boris@gmail.com', 'name': 'Boris Martins'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_user/', {'email': 'quimze@gmail.com', 'name': 'Quim Ze'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		"""  Invoke REST method to list all users  """
		r = self.client.get('/list_user/', format = 'json')
		print '\nUsers in the system:\n' + r.content


	"""  Test that POSTs 4 songs into the system  """
	def test_add_songs(self):
		"""  Invoke REST method to add a song  """
		r = self.client.post('/add_song/', {'title': 'Carry Me', 'artist': 'Bombay Bicycle Club', 'album': 'So Long, See You Tomorrow'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_song/', {'title': 'Cume', 'artist': 'Paus', 'album': 'Clarao'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_song/', {'title': 'Amor Combate', 'artist': 'Linda Martini', 'album': 'Olhos de Mongol'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_song/', {'title': 'Cigarrettes and Loneliness', 'artist': 'Chet Faker', 'album': 'Thinking in Textures'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		"""  Invoke REST method to list all songs  """
		r = self.client.get('/list_song/', format = 'json')
		print '\nSongs in the system:\n' + r.content


	"""  Test that POSTs 4 likes into the system  """
	def test_add_likes(self):
		"""  Invoke REST method to add a user  """
		r = self.client.post('/add_user/', {'email': 'ernesto@gmail.com', 'name': 'Ernesto Valverde'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_user/', {'email': 'rufino@gmail.com', 'name': 'Joao Rufino'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_user/', {'email': 'boris@gmail.com', 'name': 'Boris Martins'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_user/', {'email': 'quimze@gmail.com', 'name': 'Quim Ze'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		"""  Invoke REST method to add a song  """
		r = self.client.post('/add_song/', {'title': 'Carry Me', 'artist': 'Bombay Bicycle Club', 'album': 'So Long, See You Tomorrow'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_song/', {'title': 'Cume', 'artist': 'Paus', 'album': 'Clarao'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_song/', {'title': 'Amor Combate', 'artist': 'Linda Martini', 'album': 'Olhos de Mongol'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_song/', {'title': 'Cigarrettes and Loneliness', 'artist': 'Chet Faker', 'album': 'Thinking in Textures'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		"""  Invoke REST method to associate a song to a user (likes)  """
		r = self.client.post('/add_likes/', {'user':'quimze@gmail.com', 'song':1})
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_likes/', {'user':'quimze@gmail.com', 'song':2})
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_likes/', {'user':'quimze@gmail.com', 'song':3})
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/add_likes/', {'user':'boris@gmail.com', 'song':1})
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		"""  This user doesn't exist so the request should not be fulfilled  """
		r = self.client.post('/add_likes/', {'user':'nonexistent@gmail.com', 'song':1})
		self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)


		"""  Invoke REST method to list all likes  """
		r = self.client.get('/list_likes/', format = 'json')
		print '\nLikes in the system:\n' + r.content


