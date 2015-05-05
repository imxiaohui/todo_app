from django.db import models

CHOICE_PRIORITY = (
	(0, "Minimal"),
	(1, "Low"),
	(2, "Normal"),
	(3, "High"),
	(4, "Urgent"),
)

class Tag(models.Model):
	""" A tag representation linked to one or more tasks.
		Tags can be a location, a project, a group of people, or anything
		else that would logically group tasks.
	"""
	name = models.TextField()
	user = models.ManyToManyField(User)

class Reminder(models.Model):
	""" A reminder with a time. """
	time = models.DateTimeField()
	user = models.ManyToManyField(User)

class Task(models.Model):
	""" The base object in any task list.
		This has a description, due date and time, duration, priority, reminders, and tags.
	"""
	description = models.CharField(max_length=255)
	user = models.ManyToManyField(User)
	due = models.DateTimeField()
	duration = models.DurationField()
	priority = models.IntegerField(choices=CHOICE_PRIORITY)
	reminders = models.ManyToManyField(Reminder)
	tags = models.ManyToManyField(Tag)
