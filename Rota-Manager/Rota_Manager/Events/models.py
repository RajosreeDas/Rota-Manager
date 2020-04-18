from django.db import models


class Event(models.Model):
	name = models.CharField(max_length=100, unique=True)
	avenue = models.CharField(max_length=191)
	chair = models.CharField(max_length=100)
	secretary = models.CharField(max_length=100, blank=True, null=True)
	description = models.TextField()
	report = models.URLField(blank=True, null=True)
	remarks = models.TextField()