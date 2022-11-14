from cProfile import label
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
# print("Files in %r: %s" % (cwd, files))
df = pd.read_excel('all_features_2020.xlsx')

print(df.head())


lat = df['Lat'][:].values
lon = df['Long'][:].values
ntl = df['Light'][:].values
# lon, lat = np.meshgrid(lon, lat)
for i in range(1,4):
 labels = []
 for j in range(len(lat)):
  if ntl[j] >= 0 and ntl[j]<i:
   # print(1)
   labels.append(0)
  elif ntl[j] <= 9 and ntl[j] >= i:
   labels.append(2)
  elif ntl[j]>9:
   # print(1)
   labels.append(1)
 fig = plt.figure(figsize=(12,9))
 
 m = Basemap(projection='mill',
            llcrnrlat = 16.930,
            urcrnrlat = 17.930,
            llcrnrlon = 78.005,
            urcrnrlon = 79.055,
            resolution = 'c')
 m.drawcoastlines()

 x, y = m(list(df['Long']), list(df['Lat']))
 m.scatter(x, y,
           c = labels,
           s = 100,
           cmap = 'RdBu_r')

 plt.colorbar()

 m.drawparallels(np.arange(17.10,17.80,0.05),labels=[True,False,False,False])
 m.drawmeridians(np.arange(78,78.9,0.1),labels=[0,0,0,1])
 plt.title('[0]Rural - [0,'+str(i)+') [2]PeriUrban - ['+str(i)+',9] [1]Urban - (9,120]')
 plt.show()
