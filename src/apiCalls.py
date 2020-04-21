import requests
from dotenv import load_dotenv
import json, requests
import os
load_dotenv()

def getAirport(city):
 
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id=os.getenv("clientID"),
        client_secret=os.getenv("clientSecret"),
        v='20200419',
        query="International Airport",
        near=city,
        limit=3
    )
    resp = requests.get(url=url, params=params)

    data=json.loads(resp.text)
    return data

def getStarbucks(city):
 
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id=os.getenv("clientID"),
        client_secret=os.getenv("clientSecret"),
        v='20200419',
        query="Starbucks",
        near=city,
    )
    resp = requests.get(url=url, params=params)
    
    data=json.loads(resp.text)
    return data

def getNear(lat,lon,radius,query):
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id=os.getenv("clientID"),
        client_secret=os.getenv("clientSecret"),
        v='20200419',
        ll=f'{lat},{lon}',
        query=query,
        radius =radius,
        limit=3
    )
    resp = requests.get(url=url, params=params)
    data=json.loads(resp.text)
    return data
