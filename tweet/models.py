from django.db import models

# Create your models here.
class Tweets(models.Model):
    """
    Tweet Model
    """
    tweet_name = models.CharField(max_length=255,help_text='Enter the Tweet Name')
    tweet_content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)