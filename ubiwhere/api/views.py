# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import User, Song, Likes
from api.serializers import UserSerializer, SongSerializer, LikesSerializer
from django.http import HttpResponse, HttpRequest
import json


"""  Lists all the API's methods  """
def index(request):
	return HttpResponse('<h1>API</h1><a href="/api/list_user/">List Users</a><br><a href="/api/add_user/">Add User</a> - Provide email and name (JSON)<br><a href="/api/user/">User Update, Delete, Get</a> - URL Args needed: e-mail<br><br><a href="/api/list_song/">List Songs</a><br><a href="/api/add_song/">Add Song</a> - Provide title, artist and album (JSON)<br><a href="/api/song/">Song Update, Delete, Get</a> - URL Args needed: id<br><br><a href="/api/list_likes/">List Likes</a><br><a href="/api/add_likes/">Add Likes</a> - Provide user (email) and song (id) (JSON)<br><br>Tests provided on django project (python manage.py test)')


"""  Method to list all the users in the DB. It's serialized, so it can be read in JSON...  """
@api_view(['GET'])
def user_list(request, format = None):
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many = True)
		return Response(serializer.data)

"""  Method to add a user to the DB. Accepts data that can be serialized by UserSerializer  """
@api_view(['POST'])
def add_user(request):
	serializer = UserSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status = status.HTTP_201_CREATED)
	else:
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

"""  Method to manipulate one user in the DB. Requires Primary Key  """
@api_view(['GET', 'PUT', 'DELETE'])
def user(request, email):
	try:
		user = User.objects.get(email=email)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UserSerializer(user)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)






"""  Method to list all the songs in the DB. It's serialized, so it can be read in JSON...  """
@api_view(['GET'])
def song_list(request, format = None):
	if request.method == 'GET':
		songs = Song.objects.all()
		serializer = SongSerializer(songs, many = True)
		return Response(serializer.data)

"""  Method to add a song to the DB. Accepts data that can be serialized by SongSerializer  """
@api_view(['POST'])
def add_song(request):
	serializer = SongSerializer(data = request.data)	
	
	if serializer.is_valid():

		"""  Check if the song already exists  """
		jdict = json.loads(json.dumps(request.data))
		if len(Song.objects.all().filter(title__iexact = jdict['title']).filter(artist__iexact = jdict['artist']).filter(album__iexact = jdict['album'])) > 0:
			return Response(serializer.data, status = status.HTTP_200_OK)

		serializer.save()
		return Response(serializer.data, status = status.HTTP_201_CREATED)
	else:
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

"""  Method to manipulate one song in the DB. Requires Primary Key  """
@api_view(['GET', 'PUT', 'DELETE'])
def song(request, songid):
	try:
		song = Song.objects.get(id=songid)
	except Song.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SongSerializer(song)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SongSerializer(song, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		song.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)










"""  Method to list all the likes in the DB. It's serialized, so it can be read in JSON...  """
@api_view(['GET'])
def likes_list(request, format = None):
	if request.method == 'GET':
		likes = Likes.objects.all()
		serializer = LikesSerializer(likes, many = True)
		return Response(serializer.data)


"""  Method to add a like to the DB. Accepts data that can be serialized by LikesSerializer  """
@api_view(['POST'])
def add_likes(request):
	serializer = LikesSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status = status.HTTP_201_CREATED)
	else:
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
