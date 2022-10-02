import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Tweets
from .serializers import TweetSerializer


# initialize the APIClient app
client = Client()


class GetAllTweetTest(TestCase):
    """ Test module for GET all Tweet API """

    def setUp(self):
        Tweets.objects.create(
            tweet_name='tweet_name1', tweet_content='A Tweet may contain photos, GIFs, videos, links, and text.')
        Tweets.objects.create(
            tweet_name='tweet_name2', tweet_content='A Tweet may contain photos, GIFs, videos, links, and text.')
        Tweets.objects.create(
            tweet_name='tweet_name3', tweet_content='A Tweet may contain photos, GIFs, videos, links, and text.')
        Tweets.objects.create(
            tweet_name='tweet_name4', tweet_content='A Tweet may contain photos, GIFs, videos, links, and text.')

    def test_get_all_tweets(self):
        # get API response
        response = client.get(reverse('get_post_tweets'))
        # get data from db
        tweets = Tweets.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleTweetTest(TestCase):
    """ Test module for GET single puppy API """

    def setUp(self):
        self.tweet1 = Tweets.objects.create(
            tweet_name='Tweet 1', tweet_content='A Tweet may contain photos, GIFs, videos, links, and text.')
        self.tweet2 = Tweets.objects.create(
            tweet_name='Tweet 2', tweet_content='A Tweet may contain photos, GIFs, videos, links, and text.')
        self.tweet3 = Tweets.objects.create(
            tweet_name='Tweet 3',tweet_content='A Tweet may contain photos, GIFs, videos, links, and text.')
        self.tweet4 = Tweets.objects.create(
            tweet_name='Tweet 4', tweet_content='A Tweet may contain photos, GIFs, videos, links, and text.')

    def test_get_valid_single_tweet(self):
        response = client.get(
            reverse('get_delete_update_tweets', kwargs={'pk': self.tweet1.pk}))
        tweets = Tweets.objects.get(pk=self.tweet1.pk)
        serializer = TweetSerializer(tweets)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_tweet(self):
        response = client.get(
            reverse('get_delete_update_tweets', kwargs={'pk': 25}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewTweetTest(TestCase):
    """ Test module for inserting a new Tweet """

    def setUp(self):
        self.valid_payload = {
            'tweet_name': 'Tweet1',
            'tweet_content': 'A Tweet may contain photos, GIFs, videos, links',
           

        }
        self.invalid_payload = {
            'name': '',
            'tweet_content': 'A Tweet may contain photos, GIFs, videos, links',
            
        }

    def test_create_valid_tweet(self):
        response = client.post(
            reverse('get_post_tweets'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_tweet(self):
        response = client.post(
            reverse('get_post_tweets'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleTweetTest(TestCase):
    """ Test module for updating an existing Tweet record """

    def setUp(self):
        self.Tweet1 = Tweets.objects.create(
            tweet_name='Tweet1', tweet_content= 'A Tweet may contain photos, GIFs, videos, links')
        self.Tweet2 = Tweets.objects.create(
            tweet_name='Tweet1', tweet_content= 'A Tweet may contain photos, GIFs, videos, links')
        self.valid_payload = {
            'tweet_name': 'Tweet1',
            'tweet_content': 'A Tweet may contain lots of data',
           
        }
        self.invalid_payload = {
            'tweet_name': '',
            'tweet_content': 'No data available',
            
        }

    def test_valid_update_tweet(self):
        response = client.put(
            reverse('get_delete_update_tweets', kwargs={'pk': self.Tweet2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_tweet(self):
        response = client.put(
            reverse('get_delete_update_tweets', kwargs={'pk': self.Tweet2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleTweetTest(TestCase):
    """ Test module for deleting an existing Tweet record """

    def setUp(self):
        self.Tweet1 = Tweets.objects.create(
            tweet_name='Tweet1', tweet_content='A Tweet may contain photos, GIFs, videos, links')
        self.Tweet2 = Tweets.objects.create(
            tweet_name='Tweet2', tweet_content='A Tweet may contain photos, GIFs, videos, links')

    def test_valid_delete_tweet(self):
        response = client.delete(
            reverse('get_delete_update_tweets', kwargs={'pk': self.Tweet2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_tweet(self):
        response = client.delete(
            reverse('get_delete_update_tweets', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)