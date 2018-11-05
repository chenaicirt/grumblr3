from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    body = models.TextField()
    date_posted = models.DateTimeField(
            default=timezone.now)

class Comment(models.Model):
	post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')

	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text