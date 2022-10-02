from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tweets
from .serializers import TweetSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

@login_required
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_tweets(request, pk):
    permission_classes = [IsAuthenticated]
    authentication_classes = []
    try:
        tweets =  Tweets.objects.get(pk=pk)
    except Tweets.DoesNotExist:
        return Response({"error:Data not found"},status=status.HTTP_404_NOT_FOUND)

    # get details of a single tweet
    if request.method == 'GET':
        serializer = TweetSerializer(tweets)
        return Response(serializer.data)
        # update details of a single tweet
    if request.method == 'PUT':
        serializer = TweetSerializer(tweets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete a single tweet
    elif request.method == 'DELETE':
        tweets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@login_required
@api_view(['GET', 'POST'])
def get_post_tweets(request):
    # get all experiments
    if request.method == 'GET':
        tweets = Tweets.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
    # insert a new record for a experiment
    if request.method == 'POST':
        data = {
            'tweet_name': request.data.get('tweet_name'),
            'tweet_content': request.data.get('tweet_content'),
        }
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
