import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# %matplotlib inline
from sklearn.cluster import KMeans
df = pd.read_excel('all_features_2013.xlsx')

print(df.head())

X = df
X.drop(['Lat','Long'],axis=1,inplace=True)
kmeans = KMeans(n_clusters= 3)
 
#predict the labels of clusters.
label = kmeans.fit_predict(X)
 
print(label)
df = pd.read_excel('all_features_2013.xlsx')
df['Label'] = label
df.to_csv('all_features_2013_clustered.csv', encoding = 'utf-8-sig') 