from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.CharField( max_length= 200)
	body = models.TextField()
	pub_date = models.DateTimeField(blank=True, null=True)
	created_at = models.DateTimeField(default=timezone.now())

	def publish(self):
		self.pub_date = timezone.now()

	def __str__(self):
		return self.title
