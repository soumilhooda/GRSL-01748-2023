import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
from mpl_toolkits.basemap import Basemap

# import seaborn as sns
# from descartes import PolygonPatch
import matplotlib.pyplot as plt
# import shapefile
import pandas as pd

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
df = pd.read_excel('all_features_2020_clustered.xlsx')

print(df.head())

# print(df[1][0])
# df = df.astype({1:'float'})
# df = df.astype({2:'float'})
# df = df.astype({3:'float'})

# map = plt.contourf(x, y , mtoc_local.T, vmin=210, vmax=350,  cmap='RdPu')
# lat = df['Lat '].iloc[:].values
# lon = df['Long'].iloc[:].values
# road = df['Label'].iloc[:].values
# X, Y = np.meshgrid(loc_lon, loc_lat)
# x,y = map(X,Y)
# [X, Y] = np.meshgrid(lat, lon)


lat = df['Lat '][:].values
lon = df['Long'][:].values
# lon, lat = np.meshgrid(lon, lat)
labels = df['Label'][:].values

# m = Basemap(llcrnrlon=78.005,llcrnrlat=16.930,urcrnrlon=79.050,urcrnrlat=17.930,resolution='i',projection='merc')
# m.drawcoastlines(color = 'black')

# x, y = m(list(df['Lat ']), list(df['Long']))
# m.scatter(x, y,
#           c = df['Label'],
#           s = 100,
#           cmap = 'RdBu_r')

# plt.colorbar()
# plt.show()
fig = plt.figure(figsize=(12,9))

m = Basemap(projection='mill',
           llcrnrlat = 16.930,
           urcrnrlat = 17.930,
           llcrnrlon = 78.005,
           urcrnrlon = 79.055,
           resolution = 'c')
m.drawcoastlines()

x, y = m(list(df['Long']), list(df['Lat ']))
m.scatter(x, y,
          c = df['Label'],
          s = 100,
          cmap = 'RdBu_r')

plt.colorbar()

m.drawparallels(np.arange(17.10,17.80,0.05),labels=[True,False,False,False])
m.drawmeridians(np.arange(78,78.9,0.1),labels=[0,0,0,1])
plt.title('2020')
plt.show()

# fig, ax = plt.subplots(1, 1)
# ax.tricontourf(list(lat), list(lon), list(labels))
# ax.tricontourf(list(lat), list(lon), list(labels), cmap='rainbow')
# ax.set_title('Contour Plot')

# X, Y = np.meshgrid(lon, lat)
# x,y = map(X,Y)
# map = plt.tricontourf(list(lat), list(lon), list(labels), vmin=0, vmax=2,  cmap='RdPu')
# plt.show()

# png1 = BytesIO()
# fig.savefig(png1, format='png')

# # (2) load this image into PIL
# png2 = Image.open(png1)

# # (3) save as TIFF
# png2.save('3dPlot.tiff')
# png1.close()
# plt.show()