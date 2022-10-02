from rest_framework import serializers
from .models import Tweets


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ('pk','tweet_name', 'tweet_content','created_at', 'updated_at')