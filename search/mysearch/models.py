# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length = 50)
	content = models.TextField()
	imgurl = models.CharField(max_length = 50, default ="")
	identity = models.IntegerField(default = 0)
	nationality = models.CharField(max_length = 100, default = "")
	born = models.CharField(max_length = 100, default = "")
	occupation = models.CharField(max_length = 100, default = "")

	def __unicode__(self):
		return self.name


class KeyList(models.Model):
	key = models.CharField(max_length = 50)
	list = models.CharField(max_length = 5000, default = "")

	def __unicode__(self):
		return self.key

