# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class User(models.Model):
	email_id = models.CharField(max_length=50,unique=True)
	user_id = models.CharField(max_length=200,unique=True)
	passwd = models.CharField(max_length=200)
	
	def __str__(self):
		return self.user_id


