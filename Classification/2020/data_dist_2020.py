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

print(df.head())

 
# figure, axis = plt.subplots(2, 2)


lat = df['Lat'][:].values
lon = df['Long'][:].values
road_val = df['Road'][:].values

# road_val[road_val!=0]

print(df.describe())

kwargs = dict(alpha=0.5, bins=100)

# fig = plt.figure()
plt.hist(road_val, **kwargs, color='g', label='Road')
# plt.hist(x2, **kwargs, color='b', label='Fair')
# plt.hist(x3, **kwargs, color='r', label='Good')
plt.gca().set(title='Frequency Histogram',ylabel='Frequency')
plt.xlabel('Road Density')
plt.xlim(0,15600)
plt.legend()
plt.show()

# fig.show()

# fig2 = plt.figure()

plt.hist(df['Light'][:].values, **kwargs, color='b', label='Light')
# plt.hist(x3, **kwargs, color='r', label='Good')
plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
plt.xlabel('NTL')
plt.legend()
plt.show()
