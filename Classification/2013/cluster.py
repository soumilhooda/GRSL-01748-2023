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

df = pd.read_excel('all_features_2013.xlsx')

print(df.head())

X = df
X.drop(['Lat','Long','NDVI','LULC','Light'],axis=1,inplace=True)
d = preprocessing.normalize(X)
X = pd.DataFrame(X)
kmeans = KMeans(n_clusters= 3)

#predict the labels of clusters.
label = kmeans.fit_predict(X)
 
print(label)
df = pd.read_excel('all_features_2013.xlsx')
df['Label'] = label
# df.to_csv('all_features_2013_clustered.csv', encoding = 'utf-8-sig') 


lat = df['Lat'][:].values
lon = df['Long'][:].values
labels = df['Label'][:].values


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
          c = df['Label'],
          s = 100,
          cmap = 'RdBu_r')

plt.colorbar()

m.drawparallels(np.arange(17.10,17.80,0.05),labels=[True,False,False,False])
m.drawmeridians(np.arange(78,78.9,0.1),labels=[0,0,0,1])
plt.title("2013")
plt.show()
