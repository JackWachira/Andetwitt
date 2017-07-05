from django.shortcuts import render
import requests
import base64
import os


def fetch_requests(request):
    if request.method == 'GET':
        access_token = getAccessToken()
        andela_data = fetchData('Andela', access_token)
        andela_kenya_data = fetchData('Andela_Kenya', access_token)
        andela_nigeria_data = fetchData('Andela_Nigeria', access_token)
        return render(request, 'index.html', context={'andela': andela_data, 'kenya': andela_kenya_data, 'nigeria': andela_nigeria_data})


def getAccessToken():
    raw_token = os.getenv('API_KEY') + ':' + os.getenv('API_SECRET')
    base64_bearer_token = base64.b64encode(raw_token)
    headers = {'Authorization': 'Basic {encoded}'.format(
        encoded=base64_bearer_token), 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    body = {'grant_type': 'client_credentials'}
    response = requests.post(
        'https://api.twitter.com/oauth2/token', headers=headers, data=body)
    return response.json().get('access_token')


def fetchData(location, access_token):
    r = requests.get(
        'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={loc}&count=10'.format(loc=location), headers={'Authorization': 'Bearer {token}'.format(token=access_token)})
    return r.json()
