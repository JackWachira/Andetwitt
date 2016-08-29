from django.core.urlresolvers import reverse
from django.conf.urls import url
from tweets.views import fetch_requests
urlpatterns = [
    url(r'^$', fetch_requests)
]
