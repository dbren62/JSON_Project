import json

infile = open("US_fires_9_14.json", "r")

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
"""
brightnesses.sort()
"""
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[.03*brightness for brightness in brightnesses],
        'color':brightnesses,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]

my_layout = Layout(title="US Fires 9/14/2020 through 9/30/2020")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="US_fires.html")