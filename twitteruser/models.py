from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class TwitterUser(AbstractUser):
    position = models.CharField(max_length=120, blank=True, null=True)
    REQUIRED_FIELDS = ['position']

    def __str__(self):
        return self.username



class Follow(models.Model):
    user = models.ForeignKey(TwitterUser, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(TwitterUser, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


