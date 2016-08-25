from __future__ import unicode_literals

from django.db import models


class Tweet(models.Model):
    text = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)
