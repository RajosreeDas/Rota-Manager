from django.db import models



MEETING_CHOICES = (
		('BOARD', 'Board'),
		('REGULAR', 'Regular'),
	)


class Meeting(models.Model):
	number = models.IntegerField(null=True)
	type = models.CharField(max_length=20, choices=MEETING_CHOICES, default='REGULAR')
	agenda = models.TextField()
	date = models.DateField()
	venue = models.CharField(max_length=100)
	time = models.TimeField()
	minutes = models.URLField()
	resolutions = models.TextField(blank=True, null=True)
	attendance=models.IntegerField()
    
  
