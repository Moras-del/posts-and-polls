from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Poll(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_polls")
    total_votes = models.PositiveIntegerField(null=True, default=0)
    voters = models.ManyToManyField(User, related_name="voted_polls")

    def new_total_vote(self):
        self.total_votes += 1

    def str(self):
        return self.title

    class Meta:
        ordering = ('-date',)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def newvote(self):
        self.votes += 1
        self.poll.new_total_vote()

    def str(self):
        return self.text

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.poll.save()

# Create your models here.
