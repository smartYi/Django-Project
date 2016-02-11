from django.contrib import admin
from django.db import models
#Imprt model form models.py
from .models import Post


# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'timestamp')

	class Mets:
		model = Post
		

admin.site.register(Post, PostModelAdmin)