import pandas as pd
import numpy as np
from sklearn.ensemble import HistGradientBoostingRegressor
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# %matplotlib inline
from mpl_toolkits.basemap import Basemap
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.cluster import AgglomerativeClustering

df = pd.read_excel('all_features_2020.xlsx')

#forest 1
#grassland 2
#water body 3
#crop land 4
#urban+built-up 5
# print(df.head())
lulc_mod =[]
for i in range(len(df['LULC'])):
 if df['LULC'][i] in {11,12,13,14,15,16,17}:
  lulc_mod.append(1)
 elif df['LULC'][i] in {8,9,10}:
  lulc_mod.append(2)
 elif df['LULC'][i] == 7:
  lulc_mod.append(3)
 elif df['LULC'][i] in {4,6}:
  lulc_mod.append(4)
 elif df['LULC'][i]==5:
  lulc_mod.append(5)
  print(1)
 
df['LULC_mod'] = lulc_mod
# df.to_excel("LULC_mod.xlsx")
# print(df['LULC'].describe())
print(df['LULC_mod'].describe())
lat = df['Lat'][:].values
lon = df['Long'][:].values
# lon, lat = np.meshgrid(lon, lat)
labels = df['LULC_mod'][:].values

# m = Basemap(llcrnrlon=78.005,llcrnrlat=16.930,urcrnrlon=79.050,urcrnrlat=17.930,resolution='i',projection='merc')
# m.drawcoastlines(color = 'black')

# x, y = m(list(df['Lat ']), list(df['Long']))
# m.scatter(x, y,
#           c = df['Label'],
#           s = 100,
#           cmap = 'RdBu_r')

# plt.colorbar()
# plt.show()
# fig = plt.figure(figsize=(12,9))

# m = Basemap(projection='mill',
#            llcrnrlat = 16.930,
#            urcrnrlat = 17.930,
#            llcrnrlon = 78.005,
#            urcrnrlon = 79.055,
#            resolution = 'c')
# m.drawcoastlines()

# x, y = m(list(df['Long']), list(df['Lat']))
# m.scatter(x, y,
#           c = df['LULC_mod'],
#           s = 100,
#           cmap = 'RdBu_r')

# plt.colorbar()

# m.drawparallels(np.arange(17.10,17.80,0.05),labels=[True,False,False,False])
# m.drawmeridians(np.arange(78,78.9,0.1),labels=[0,0,0,1])
# plt.title('2020')
# plt.show()
