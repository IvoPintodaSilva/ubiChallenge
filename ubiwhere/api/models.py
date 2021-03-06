from django.db import models


"""  A model is a source of information about the data  """



"""  User is identified by his email  """
class User(models.Model):
	def __str__(self):
		return self.email

	name = models.CharField(max_length=50)
	email = models.EmailField(primary_key = True)





"""  A song cannot be defined by the title, artist or name. The primary key will be a numerical id  """
class Song(models.Model):
	def __str__(self):
		return self.artist.encode('utf-8') + ' - ' + self.title.encode('utf-8')


	"""  Django gives each model the following field: id = models.AutoField(primary_key=True)  """
	title = models.CharField(max_length=50)
	artist = models.CharField(max_length=20)
	album = models.CharField(max_length=50)




"""  One user can like many songs  """
class Likes(models.Model):
	def __str__(self):
		return str(self.user) + ' likes: ' + str(self.song)

	user = models.ForeignKey(User)
	song = models.ForeignKey(Song)


