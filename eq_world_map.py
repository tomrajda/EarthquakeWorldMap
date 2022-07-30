import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Analysis data structure
file_name = 'project_2/chapter_16/World_Earthquakes_Map/4.5_month.json'
with open (file_name, encoding="utf-8") as f:
    all_eq_data = json.load(f)

#readable_file = 'project_2/chapter_16/data/readable_eq_data.json'
#with open(readable_file, 'w') as f:
    #json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']

mags = []
lons = []
lats = []
hover_texts = []
for eq_dict in all_eq_dicts:
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    mags.append(eq_dict['properties']['mag'])
    hover_texts.append(eq_dict['properties']['title'])

# Visualization earthquake map
title_1 = all_eq_data['metadata']['title']
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [3*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Richter scale'},
    },
}]

my_layout = Layout(title=title_1)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

