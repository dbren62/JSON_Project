import json

infile = open("US_fires_9_1.json", "r")

fire_data = json.load(infile)

list_of_fires = fire_data

brightnesses, lons, lats = [], [], []

for fire in list_of_fires:
    brightness = fire["brightness"]
    lon = fire["longitude"]
    lat = fire["latitude"]

    if brightness >= 450:
        brightnesses.append(brightness)
        lons.append(lon)
        lats.append(lat)

print(brightnesses[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[5*brightness for brightness in brightnesses],
        'color':brightness,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]
