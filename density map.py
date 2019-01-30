import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import pandas as pd
import numpy as np
import matplotlib
# create the map
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,projection='lcc',lat_1=33,lat_2=45,lon_0=-95) # load the shapefile, use the name 'states'
# download from https://github.com/matplotlib/basemap/tree/master/examples/st99_d00.dbf,shx,shp
map.readshapefile('st99_d00', name='states', drawbounds=True)
# collect the state names from the shapefile attributes so we can
# look up the shape obect for a state by it's name
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])
ax = plt.gca() # get current axes instance
# load density data drawn from
# https://en.wikipedia.org/wiki/List_of_U.S._states_by_population_density
df = pd.read_csv('states.csv')
# determine the range of density values
max_density = -1.0
min_density = -1.0
for index, row in df.iterrows():
    d = row['density/mi2']
    density = float(d.replace(',' , ''))
    if (max_density==-1.0) or (max_density<density):
        max_density = density
    if (min_density==-1.0) or (min_density>density):
        min_density = density
print('max',max_density)
print('min',min_density)
range_density = max_density - min_density
print(range_density)
# we pick a color for the state density out of red spectrum
cmap = matplotlib.cm.get_cmap('Spectral')
# for each state get the color for it's density
for index, row in df.iterrows():
    state_name = row['State']
    d = row['density/mi2']
    density = float(d.replace(',' , ''))
    color = cmap((density - min_density)/range_density)
    seg = map.states[state_names.index(state_name)]
    poly = Polygon(seg, facecolor=color, edgecolor=color)
    ax.add_patch(poly)
plt.show()