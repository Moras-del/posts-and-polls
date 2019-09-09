from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Poll(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
	num_of_choices = models.PositiveIntegerField(null=True)
	total_votes = models.PositiveIntegerField(null=True, default=0)

	def new_total_vote(self):
		self.total_votes += 1

	def __unicode__(self):
		return self.title

	class Meta:
		permissions = (('can_vote_poll','can_vote_poll')),

class Choices(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def newvote(self):
		self.votes += 1

	def __unicode__(self):
		return self.choice_text

# Create your models here.
