from django.contrib import admin

# Register your models here.

from .models import User, Song, Likes

admin.site.register(User)
admin.site.register(Song)
admin.site.register(Likes)