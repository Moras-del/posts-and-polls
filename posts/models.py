from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length = 20)
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
	pluses = models.PositiveIntegerField(default=0)
	class Meta:
		permissions = (('can_plus_post','can_plus_post')),

class Comment(models.Model):
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)	
# Create your models here.
