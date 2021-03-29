import requests
from django.shortcuts import render
from urllib.request import urlopen
import json


def home(request):
    data = []
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"Turkey"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "0b46caccbemshb9de52da74da2b3p139ccejsna46aa49eeaaf"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    d = response['response']
    s = d[0]

    context = {
        'all': s['cases']['total'],
        'recovered': s['cases']['recovered'],
        'deaths': s['deaths']['total'],
        'new': s['cases']['new'],
        'serioz': s['cases']['critical'],
    }
    
   

    return render(request, 'index.html', context)
