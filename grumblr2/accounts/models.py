from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model): 
	user = models.OneToOneField(User,on_delete=models.CASCADE,
        primary_key=True)
	bio = models.CharField(max_length = 420, default = '')
	age = models.IntegerField(default = 1)
	image = models.ImageField(upload_to = 'photos/', blank = True, null = True)

	def _str_(self):
		return self.user

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()



class Follower(models.Model):
	users = models.ManyToManyField(UserProfile)
	current_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name="owner", null=True)

	@classmethod
	def make_follower(cls, current_user, new_follower):
	    follower, created = cls.objects.get_or_create(
	        current_user = current_user
	    )
	    follower.users.add(new_follower)

	@classmethod
	def remove_follower(cls, current_user, new_follower):
	    follower, created = cls.objects.get_or_create(
	        current_user = current_user
	    )
	    follower.users.remove(new_follower)

	def __str__(self):
	    return str(self.current_user)
