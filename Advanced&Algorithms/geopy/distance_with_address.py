import requests
import urllib.parse
from math import radians, cos, sin, asin, sqrt

address = input('What is your start location? - (street,lane,road) : ')
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json' #Uses nomination and searches query

response1 = requests.get(url).json()
lat1 = (response1[0]["lat"])
lon1 = (response1[0]["lon"])
print(lat1, lon1)

import requests
import urllib.parse
from math import radians, cos, sin, asin, sqrt
address2 = input("What is your end location? : ")
url2 = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address2) +'?format=json'

response2 = requests.get(url2).json()
lat2 = (response2[0]["lat"])
lon2 = (response2[0]["lon"])
print(lat2, lon2)

from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # 6367 km (3961 miles) is the radius of the Earth
    km = 6367 * c
    miles = 3961 * c
    return km, miles

lat1 = float(lat1)
lon1 = float(lon1)
lat2 = float(lat2)
lon2 = float(lon2)
km, miles = haversine(lon1, lat1, lon2, lat2)
sf = "The distance between {} and {} is {:0.1f} km (air)"
print(sf.format(address, address2, km))
