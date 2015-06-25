from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import User, Song, Likes
from api.serializers import UserSerializer, SongSerializer, LikesSerializer





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
		serializer = SnippetSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)