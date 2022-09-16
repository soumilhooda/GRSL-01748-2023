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

# df_road = pd.read_csv('road2013-2020.ascii')
# df_light = pd.read_csv('light2013-2020.ascii')
# df_lulc = pd.read_csv('lulc2013-2020.csv',header=None)
# df_ndvi = pd.read_csv('ndvi2013-2020.csv',header=None)

df_light = pd.read_csv("light2013-2020.ascii", delim_whitespace=" ", header=None)
df_lulc = pd.read_csv("lulc2013-2020.ascii", delim_whitespace=" ", header=None)
df_ndvi = pd.read_csv("ndvi2013-2020.ascii", delim_whitespace=" ", header=None)
df_road = pd.read_csv("road2013-2020.ascii", delim_whitespace=" ", header=None)
features = [0,1,2,3,4,5,6,7,8,9]
df_light.columns = features
df_lulc.columns = features
df_ndvi.columns = features
df_road.columns = features

df_lulc = df_lulc.append({0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},ignore_index=True)
df_ndvi = df_ndvi.append({0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},ignore_index=True)

print(df_light.shape[0])
print(df_lulc.shape[0])
print(df_ndvi.shape[0])
print(df_road.shape[0])
print(df_lulc.tail())

for i in range(9,10):
 df = pd.DataFrame()
 df['Road'] = df_road[i][:].values
 df['Light'] = df_light[i][:].values
 df['LULC'] = df_lulc[i][:].values
 df['NDVI'] = df_ndvi[i][:].values
 # df.fillna(0)
 X = df
 print(X.isnull().values.any())
 d = preprocessing.normalize(X)
 X = pd.DataFrame(X)
 
 clustering = AgglomerativeClustering(n_clusters=3)
 #predict the labels of clusters.
 label = clustering.fit_predict(X)
 # print(type(label))
 # label^(label&1==label)
 for j in range(len(label)):
  if label[j] == 2:
   label[j] =0
  elif label[j]==0:
   label[j]=2
 #  elif label[j]==1:
 #   label[j] = 0
 df['Label'] = label
 lat = df_road[0][:].values
 lon = df_road[1][:].values
 labels = df['Label'][:].values


 fig = plt.figure(figsize=(12,9))

 m = Basemap(projection='mill',
            llcrnrlat = 16.930,
            urcrnrlat = 17.930,
            llcrnrlon = 78.005,
            urcrnrlon = 79.055,
            resolution = 'c')
 m.drawcoastlines()

 x, y = m(list(df_road[1]), list(df_road[0]))
 m.scatter(x, y,
           c = df['Label'],
           s = 100,
           cmap = 'RdBu_r')

 plt.colorbar()

 m.drawparallels(np.arange(17.10,17.80,0.05),labels=[True,False,False,False])
 m.drawmeridians(np.arange(78,78.9,0.1),labels=[0,0,0,1])
 plt.title(str(i+2011)+"_agglomerative")
 plt.show()
 # plt.savefig(str(i+2011)+'_agg.png')



# X = df
# d = preprocessing.normalize(X)
# X = pd.DataFrame(X)
# clustering = AgglomerativeClustering(n_clusters=3)

# #predict the labels of clusters.
# label = clustering.fit_predict(X)
 
# print(label)
# # df = pd.read_excel('all_features_2020.xlsx')
# df['Label'] = label
# # df.to_csv('all_features_2013_clustered.csv', encoding = 'utf-8-sig') 


# lat = df['Lat'][:].values
# lon = df['Long'][:].values
# labels = df['Label'][:].values


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
#           c = df['Label'],
#           s = 100,
#           cmap = 'RdBu_r')

# plt.colorbar()

# m.drawparallels(np.arange(17.10,17.80,0.05),labels=[True,False,False,False])
# m.drawmeridians(np.arange(78,78.9,0.1),labels=[0,0,0,1])
# plt.title("2020_agglomerative")
# plt.show()
