#import json, string

#import requests
#import geocoder
#import pandas as pd
import folium
import webbrowser
'''
a = input()
b = input()
m = folium.Map(location=[a, b])
'''
#########################################
"""
with open("secrets/.wmata") as fin:
    wmata_key = fin.read().strip()
location = 'Union Station, Washington, DC'
loc = geocoder.osm(location)
loc.json
latlng = [loc.lat, loc.lng]

bus_map = Map(location=latlng,
              zoom_start=15)
bus_map.add_child(Marker(location=latlng, popup=loc.address, icon = folium.Icon(color = 'blue')))
# bus_map.add_child(GeoJson(loc.geojson))
bus_map
"""
x = input()

if x == "Portland":
    a = 45.5236
    b = -122.6750
elif x == "Paris":
    a = 48.8566
    b = 2.3522
elif x == "NY":
    a = 40.7128
    b = -74.0060
elif x == "LA":
    a = 34.0522
    b = -118.2437

m = folium.Map(location=[a, b], tiles='Stamen Toner', zoom_start=13)


m.save('index.html')

new = 2
url = "file:///home/imserega/PycharmProjects/pythonProject/venv/index.html" #path to .HTML File
webbrowser.open(url, new=new)

