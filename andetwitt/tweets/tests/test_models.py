from django.test import TestCase
from tweets.models import Tweet


class TestTweet(TestCase):

    def test_create_save(self):
        tweet = Tweet()
        tweet.text = 'test_tweet'
        tweet.handle = 'test_handle'
        tweet.save()

        all_tweets = Tweet.objects.all()
        self.assertEquals(len(all_tweets), 1)
        only_tweet = all_tweets[0]
        self.assertEquals(only_tweet, tweet)
        self.assertEquals(only_tweet.text, 'test_tweet')
        self.assertEquals(only_tweet.handle, 'test_handle')
