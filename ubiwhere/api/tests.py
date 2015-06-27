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
		r = self.client.post('/api/add_user/', {'email': 'ernesto@gmail.com', 'name': 'Ernesto Valverde'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_user/', {'email': 'rufino@gmail.com', 'name': 'Joao Rufino'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_user/', {'email': 'boris@gmail.com', 'name': 'Boris Martins'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_user/', {'email': 'quimze@gmail.com', 'name': 'Quim Ze'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		"""  Invoke REST method to list all users  """
		"""  It should print to the console 4 users  """
		r = self.client.get('/api/list_user/', format = 'json')
		print '\ntest_add_users: 4 users should be displayed\nUsers in the system:\n' + r.content

	"""  Test that POSTs 4 users into the system and DELETEs 3 of them  """
	def test_delete_users(self):
		"""  Invoke REST method to add a user  """
		r = self.client.post('/api/add_user/', {'email': 'ernesto@gmail.com', 'name': 'Ernesto Valverde'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_user/', {'email': 'rufino@gmail.com', 'name': 'Joao Rufino'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_user/', {'email': 'boris@gmail.com', 'name': 'Boris Martins'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_user/', {'email': 'quimze@gmail.com', 'name': 'Quim Ze'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		r = self.client.delete('/api/user/ernesto@gmail.com')
		self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)
		r = self.client.delete('/api/user/rufino@gmail.com')
		self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)
		r = self.client.delete('/api/user/boris@gmail.com')
		self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)

		"""  Invoke REST method to list all users  """
		"""  It should print to the console 1 user  """
		r = self.client.get('/api/list_user/', format = 'json')
		print '\ntest_delete_users: 1 user should be displayed\nUsers in the system:\n' + r.content



	"""  Test that POSTs 4 songs into the system  """
	def test_add_songs(self):
		"""  Invoke REST method to add a song  """
		r = self.client.post('/api/add_song/', {'title': 'Carry Me', 'artist': 'Bombay Bicycle Club', 'album': 'So Long, See You Tomorrow'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_song/', {'title': 'Cume', 'artist': 'Paus', 'album': 'Clarao'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_song/', {'title': 'Amor Combate', 'artist': 'Linda Martini', 'album': 'Olhos de Mongol'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_song/', {'title': 'Cigarrettes and Loneliness', 'artist': 'Chet Faker', 'album': 'Thinking in Textures'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		"""  Invoke REST method to list all songs  """
		r = self.client.get('/api/list_song/', format = 'json')
		print '\ntest_add_songs: 4 songs should be displayed\nSongs in the system:\n' + r.content



	"""  Test that POSTs 4 songs into the system and DELETEs 3 of them  """
	def test_delete_songs(self):
		"""  Invoke REST method to add a song  """
		r = self.client.post('/api/add_song/', {'title': 'Carry Me', 'artist': 'Bombay Bicycle Club', 'album': 'So Long, See You Tomorrow'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_song/', {'title': 'Cume', 'artist': 'Paus', 'album': 'Clarao'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_song/', {'title': 'Amor Combate', 'artist': 'Linda Martini', 'album': 'Olhos de Mongol'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_song/', {'title': 'Cigarrettes and Loneliness', 'artist': 'Chet Faker', 'album': 'Thinking in Textures'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)


		"""  Invoke REST method to delete songs by their ID (autoincremental)  """
		r = self.client.delete('/api/song/1')
		self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)
		r = self.client.delete('/api/song/2')
		self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)
		r = self.client.delete('/api/song/3')
		self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)

		
		"""  Invoke REST method to list all songs  """
		"""  There should only remain 1 song in the system  """
		r = self.client.get('/api/list_song/', format = 'json')
		print '\ntest_delete_songs: 1 song should be displayed\nSongs in the system:\n' + r.content


	"""  Test that POSTs 4 likes into the system  """
	def test_add_likes(self):
		"""  Invoke REST method to add a user  """
		r = self.client.post('/api/add_user/', {'email': 'ernesto@gmail.com', 'name': 'Ernesto Valverde'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_user/', {'email': 'rufino@gmail.com', 'name': 'Joao Rufino'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_user/', {'email': 'boris@gmail.com', 'name': 'Boris Martins'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_user/', {'email': 'quimze@gmail.com', 'name': 'Quim Ze'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		"""  Invoke REST method to add a song  """
		r = self.client.post('/api/add_song/', {'title': 'Carry Me', 'artist': 'Bombay Bicycle Club', 'album': 'So Long, See You Tomorrow'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_song/', {'title': 'Cume', 'artist': 'Paus', 'album': 'Clarao'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_song/', {'title': 'Amor Combate', 'artist': 'Linda Martini', 'album': 'Olhos de Mongol'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_song/', {'title': 'Cigarrettes and Loneliness', 'artist': 'Chet Faker', 'album': 'Thinking in Textures'}, format='json')
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		"""  Invoke REST method to associate a song to a user (likes)  """
		r = self.client.post('/api/add_likes/', {'user':'quimze@gmail.com', 'song':1})
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_likes/', {'user':'quimze@gmail.com', 'song':2})
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_likes/', {'user':'quimze@gmail.com', 'song':3})
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)
		r = self.client.post('/api/add_likes/', {'user':'boris@gmail.com', 'song':1})
		self.assertEqual(r.status_code, status.HTTP_201_CREATED)

		"""  This user doesn't exist so the request should not be fulfilled  """
		r = self.client.post('/api/add_likes/', {'user':'nonexistent@gmail.com', 'song':1})
		self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)


		"""  Invoke REST method to list all likes  """
		r = self.client.get('/api/list_likes/', format = 'json')
		print '\ntest_add_likes: 4 Likes should be displayed\nLikes in the system:\n' + r.content


