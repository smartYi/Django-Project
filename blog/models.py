from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Core of the project

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField() #Larger area than CharField
	user = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	update = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return self.title


	def __str__(self):
		return self.title
