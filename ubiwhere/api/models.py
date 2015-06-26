from django.db import models


"""  A model is a source of information about the data  """

"""  When I ask for the primary key it will give me the email instead of the id - JSON  """
#class UserManager(models.Manager):
#    def get_by_natural_key(self, email):
#        return self.get(email=email)

"""  User is identified by his email  """
class User(models.Model):
#	objects = UserManager()

	def __str__(self):
		return self.email

	name = models.CharField(max_length=50)
	email = models.EmailField(primary_key = True)



"""  When I ask for the primary key it will give me the title, artist, album instead of the id - JSON  """
#class SongManager(models.Manager):
#    def get_by_natural_key(self, title, artist, album):
#        return self.get(title=title, artist=artist, album=album)

"""  A song cannot be defined by the title, artist or name. The primary key will be a numerical id  """
class Song(models.Model):
#	objects = SongManager()

	def __str__(self):
		return self.artist + ' - ' + self.title

	"""  Django gives each model the following field: id = models.AutoField(primary_key=True)  """
	title = models.CharField(max_length=50)
	artist = models.CharField(max_length=20)
	album = models.CharField(max_length=50)




"""  One user can like many songs  """
class Likes(models.Model):

	def __str__(self):
		return str(self.user) + '   likes:   ' + str(self.song)

	user = models.ForeignKey(User)
	song = models.ForeignKey(Song)


