from django.http import HttpResponse
from api.models import User, Song, Likes
from api.serializers import UserSerializer, SongSerializer, LikesSerializer
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from itertools import chain
import json
import re


"""  Serves a page for the user to select User, Song or Likes operations  """
def index(request):
	context = {}
	return render(request, 'webapp/index.html', context)


"""  Serves a page with the possible operations for User  """
def user(request):
	user_list = User.objects.all().order_by('email')
	context = {'user_list': user_list}
	return render(request, 'webapp/user.html', context)

"""  Serves a detailed user page when you click on the user  """
def user_details(request):
	user_email = request.GET.get('user_email', '')
	user = get_object_or_404(User, pk = user_email)
	likes_list = Likes.objects.filter(user = user)
	""" Exclude the songs that the user already likes """
	songs_to_exclude = [l.song.id for l in likes_list]
	song_list = Song.objects.all().exclude(id__in = songs_to_exclude)
	
	context={'user':user, 'likes_list':likes_list, 'song_list':song_list}
	return render(request, 'webapp/user_details.html', context)

"""  Method runs when delete button is pressed on a user  """
def user_delete(request):
	user_email = request.GET.get('user_email', '')
	user = get_object_or_404(User, pk = user_email)
	user.delete()
	context = {}
	return render(request, 'webapp/user_removed.html', context)

"""  Serves a form to introduce credentials of new user  """
def user_form(request):
	return render(request, 'webapp/user_form.html')

"""  Add user to the system """
def user_add(request):
	name = request.GET.get('name', '')
	email = request.GET.get('email', '')
	context={}
	"""  check if email is correct and name not empty  """
	if not re.match(r"[^@]+@[^@]+\.[^@]+", email) or name == '':
		return render(request, 'webapp/user_form.html', context)
	"""  check if user already exists  """
	try:
		exists = User.objects.get(email=email)
	except User.DoesNotExist:
		exists = None
		user = User(email = email, name = name)
		user.save()
		return render(request, 'webapp/user_added.html', context)
	return render(request, 'webapp/user_form.html', context)

	





"""  Serves a page with the possible operations for Song  """
def song(request):
	song_list = Song.objects.all().order_by('artist')
	context = {'song_list': song_list}
	return render(request, 'webapp/song.html', context)


"""  Method runs when delete button is pressed on a song  """
def song_delete(request):
	song_id = request.GET.get('song_id', '')
	song = get_object_or_404(Song, pk = song_id)
	song.delete()
	context = {}
	return render(request, 'webapp/song_removed.html', context)

"""  Serves a form to introduce credentials of new song  """
def song_form(request):
	return render(request, 'webapp/song_form.html')

"""  Add song to the system """
def song_add(request):
	title = request.GET.get('title', '')
	artist = request.GET.get('artist', '')
	album = request.GET.get('album', '')
	context={}
	"""  Check if title, artist or album are empty  """
	if title == '' or artist == '' or album == '':
		return render(request, 'webapp/song_form.html', context)
	"""  Check if song already exists  """
	if len(Song.objects.all().filter(title__iexact = title).filter(artist__iexact = artist).filter(album__iexact = album)) > 0:
		return render(request, 'webapp/song_form.html', context)
	song = Song(title = title, artist = artist, album = album)
	song.save()
	context={}
	return render(request, 'webapp/song_added.html', context)

"""  Serves a detailed user page when you click on the song  """
def song_details(request):
	song_id = request.GET.get('song_id', '')
	song = get_object_or_404(Song, pk = song_id)
	context={'song':song}
	return render(request, 'webapp/song_details.html', context)






"""  Serves a page with the possible operations for Likes  """
def likes(request):
	likes_list = Likes.objects.all().order_by('user')
	context = {'likes_list': likes_list}
	return render(request, 'webapp/likes.html', context)

"""  Serves a form to introduce credentials of new likes  """
def likes_form(request):
	user_list = User.objects.all().order_by('email')
	song_list = Song.objects.all().order_by('artist')
	context = {'user_list': user_list, 'song_list': song_list}
	return render(request, 'webapp/likes_form.html', context)

"""  Add likes to the system """
def likes_add(request):
	user_email = request.GET.get('dropdown_user', '')
	user = get_object_or_404(User, pk = user_email)
	song_id = request.GET.get('dropdown_song', '')
	song = get_object_or_404(Song, pk = int(song_id))
	likes = Likes(user = user, song = song)
	likes.save()
	context={}
	return render(request, 'webapp/likes_added.html', context)

"""  Method runs when delete button is pressed on a likes  """
def likes_delete(request):
	likes_id = request.GET.get('likes_id', '')
	likes = get_object_or_404(Likes, pk = likes_id)
	likes.delete()
	context = {}
	return render(request, 'webapp/likes_removed.html', context)

"""  Adds likes on user details page  """
def likes_add_onuserdetails(request):
	user_email = request.GET.get('user_email', '')
	user = get_object_or_404(User, pk = user_email)
	song_id = request.GET.get('dropdown_song','')
	song = get_object_or_404(Song, pk = int(song_id))
	likes = Likes(user = user, song = song)
	likes.save()
	likes_list = Likes.objects.filter(user = user)
	songs_to_exclude = [l.song.id for l in likes_list]
	song_list = Song.objects.all().exclude(id__in = songs_to_exclude)
	context = {'user':user, 'likes_list':likes_list, 'song_list':song_list}
	return render(request, 'webapp/user_details.html', context)
