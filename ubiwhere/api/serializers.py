from django.forms import widgets
from rest_framework import serializers
from api.models import User, Song, Likes


"""  serialize information  """


"""  Serializes User object  """
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'name')
# 	name = serializers.CharField(max_length = 50)
# 	email = serializers.EmailField(read_only=True)


# 	def create(self, validated_data):
# 		return User.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		instance.name = validated_data.get('name', instance.name)

"""  Serializes Song object  """
class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ('id', 'title', 'artist', 'album')
# 	pk = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField(max_length = 50)
# 	artist = serializers.CharField(max_length=20)
# 	album = serializers.CharField(max_length=50)


# 	def create(self, validated_data):
# 		return Song.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		instance.title = validated_data.get('title', instance.title)
# 		instance.artist = validated_data.get('artist', instance.artist)
# 		instance.album = validated_data.get('album', instance.album)


"""  Serializes Likes object  """
class LikesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Likes
		fields = ('user', 'song')
# 	# user = serializers.EmailField(read_only=True)
# 	# song = serializers.CharField(max_length = 50)


# 	# def create(self, validated_data):
# 	# 	return Likes.objects.create(**validated_data)

# 	# def update(self, instance, validated_data):
# 	# 	instance.user = validated_data.get('user', instance.user)
# 	# 	instance.song = validated_data.song('song', instance.song)


