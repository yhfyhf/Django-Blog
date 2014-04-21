# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	pub_date = models.DateField()

	def __unicode__(self):
		return u'%s %s %s' % (self.title, 
			self.content, self.pub_date)


class Tag(models.Model):
	post = models.ForeignKey(Post)
	name = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.name