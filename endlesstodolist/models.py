from django.db import models

CHOICE_PRIORITY = (
	(0, "Minimal"),
	(1, "Low"),
	(2, "Normal"),
	(3, "High"),
	(4, "Urgent"),
)

# Create your models here.
class Task(models.Model):
	""" The base object in any task list.
		This has a description, due date and time, duration, priority, reminders, and tags.
	"""
	description = models.CharField()
	due = models.DateTimeField()
	duration = models.DurationField()
	priority = models.CharField(max_length=1, choices=CHOICE_PRIORITY)
	reminders = models.ManyToManyField(Reminder)
	tags = models.ManyToManyField(Tag)
	
class Tag(models.Model):
	""" A tag representation linked to one or more tasks. 
		Tags can be a location, a project, a group of people, or anything 
		else that would logically group tasks. 
	"""
	name = models.TextField()
	
class Reminder(models.Model):
	""" A reminder with a time. """
	time = models.DateTimeField()