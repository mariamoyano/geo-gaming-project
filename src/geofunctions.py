import requests
from dotenv import load_dotenv
import json, requests
import os
load_dotenv()

def geocode(address):
    '''
    Use geocode api to do forward geocoding. https://geocode.xyz/api
    '''
    apiKey = os.getenv("geoCode_APIKEY")
    print("APIKEY FOUND!!") if apiKey else print("ERROR: NO APIKEY FOUND")
    headers = {"Authorization":f"token {apiKey}"} if apiKey else {}
    res = requests.get(f"https://geocode.xyz/{address}",params={"json":1},headers=headers)
    data = res.json()
    print(res)
    # Return as GeoJSON -> https://geojson.org/
    return {
        "type":"Point",
        "coordinates": [float(data["latt"]), float(data["longt"])]
    }
